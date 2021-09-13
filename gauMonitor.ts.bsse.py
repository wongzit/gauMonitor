# gauMonitor module TS-BSSE
# Program version: 3.0.0
# Update at 2021-09-12

import sys

def conOrNot (con1, con2, con3, con4):
	conYN = 'NNNN'
	if con1 == 'NO':
		if con2 == 'NO':
			if con3 == 'NO':
				if con4 == 'NO':
					conYN = 'NNNN'
				else:
					conYN = 'NNNY'
			else:
				if con4 == 'NO':
					conYN = 'NNYN'
				else:
					conYN = 'NNYY'
		else:
			if con3 == 'NO':
				if con4 == 'NO':
					conYN = 'NYNN'
				else:
					conYN = 'NYNY'
			else:
				if con4 == 'NO':
					conYN = 'NYYN'
				else:
					conYN = 'NYYY'
	else:
		if con2 == 'NO':
			if con3 == 'NO':
				if con4 == 'NO':
					conYN = 'YNNN'
				else:
					conYN = 'YNNY'
			else:
				if con4 == 'NO':
					conYN = 'YNYN'
				else:
					conYN = 'YNYY'
		else:
			if con3 == 'NO':
				if con4 == 'NO':
					conYN = 'YYNN'
				else:
					conYN = 'YYNY'
			else:
				if con4 == 'NO':
					conYN = 'YYYN'
				else:
					conYN = 'YYYY'
	return conYN

def eneComp (ene1, ene2):
	eneFlag = '='
	eneDiff = float(ene1) - float(ene2)
	if eneDiff < 0.00000:
		eneFlag = '+'
	elif eneDiff > 0.00000:
		eneFlag = '-'
	return eneFlag

logPath = sys.argv[1]
#logPath = '/Users/wangzhe/Desktop/tempo_ct_ts_opt_bsse.log'
jobType = sys.argv[2]
#jobType = 'optfreq'

with open(logPath, 'r') as output:
	logFile = output.readlines()

scfStart = 0
print("Optimization job has found, looking for SCF iterations data...\n")
for b in range(len(logFile)):
	if 'Threshold  Converged?' in logFile[b]:
		scfStart = 1
		threshold1 = logFile[b + 1].split()[3]
		threshold2 = logFile[b + 2].split()[3]
		threshold3 = logFile[b + 3].split()[3]
		threshold4 = logFile[b + 4].split()[3]
		break
if scfStart == 1:
	print("\n# SCF ITERATIONS\n- Summary of SCF Iterations:\n")
	print("  Cycle    Max.Force     RMS.Force       Max.DP        RMS.DP    Converged?")
	print("-----------------------------------------------------------------------------")
	print(f"           ({threshold1})    ({threshold2})    ({threshold3})    ({threshold4})  Threshold")
	convergeCount = 0
	for j in range(len(logFile)):
		if 'Threshold  Converged?' in logFile[j]:
			convergeCount += 1
			print(f"   {format(str(convergeCount).rjust(3))}      {logFile[j + 1].split()[2]}      \
{logFile[j + 2].split()[2]}      {logFile[j + 3].split()[2]}      {logFile[j + 4].split()[2]}      \
{conOrNot(logFile[j + 1].split()[4], logFile[j + 2].split()[4], logFile[j + 3].split()[4], logFile[j + 4].split()[4])}")
		if "Normal termination of Gaussian" in logFile[j]:
			break
	print("-----------------------------------------------------------------------------\n")
	scfEnergy = []
	print("\n- Summary of electronic energy:\n")
	for f in range(len(logFile)):
		if 'Counterpoise corrected energy' in logFile[f]:
			scfEnergy.append(logFile[f].split()[4])
		if "Normal termination of Gaussian" in logFile[f]:
			break
	print("  Cycle        E (Hartree)          E.rel (kcal/mol)     Delta-E")
	print("------------------------------------------------------------------")
	if len(scfEnergy) == 1:
		print(f"    1      {scfEnergy[0]}           0.000000")
	elif len(scfEnergy) > 1:
		print(f"    1      {scfEnergy[0]}           0.000000")
		for m in range(1, len(scfEnergy)):
			print(f"  {str(m + 1).rjust(3)}      {scfEnergy[m]}       {str(format(((float(scfEnergy[m]) - float(scfEnergy[0])) * 627.51), '.6f')).rjust(12)}            {eneComp(scfEnergy[m - 1], scfEnergy[m])}")
	print("------------------------------------------------------------------\n")
	
	for i in range(len(logFile)):
		if 'Initial Parameters' in logFile[i]:
			redunCoorStart = i + 5
			break
	
	redunCoor = []
	for c in range(redunCoorStart, len(logFile)):
		if '----------------' not in logFile[c]:
			redunCoor.append(logFile[c].split()[1])
			redunCoor.append(logFile[c].split()[2])
		else:
			break

	eigenValues = []
	for k in range(len(logFile)):
		if 'Counterpoise corrected energy' in logFile[k]:
			scfLine = k
			for l in range(k, len(logFile)):
				if 'Eigenvalues ---' in logFile[l]:
					eigenValues.append(logFile[l][20:].strip())
					break
		elif 'Normal termination' in logFile[k]:
			break

	eigenVactors = []
	for m in range(len(logFile)):
		if 'Eigenvectors required to have negative eigenvalues' in logFile[m]:
			eigenVactors.append(logFile[m + 1].split()[0])
			eigenVactors.append(logFile[m + 1].split()[1])
			eigenVactors.append(logFile[m + 1].split()[2])
			eigenVactors.append(logFile[m + 1].split()[3])
			eigenVactors.append(logFile[m + 1].split()[4])
			eigenVactors.append(logFile[m + 3].split()[0])
		elif 'Normal termination' in logFile[m]:
			break
	print("\n# FORCE CONSTANT\n- Summary of eigenvectors and eigenvalues\n")
	print(" Cycle   Five minimum eigenvalues")
	print("         Six eigenvectors required to have negative eigenvalues")
	print("----------------------------------------------------------------")

	for n in range(len(eigenValues)):
		print(f'  {str(n + 1).rjust(3)}', end='')
		print(f'   {eigenValues[n].rjust(48)}')
		print(f'         {redunCoor[redunCoor.index(eigenVactors[n]) + 1].ljust(20)}', end='')
		print(f'{redunCoor[redunCoor.index(eigenVactors[n + 1]) + 1].ljust(20)}', end='')
		print(f'{redunCoor[redunCoor.index(eigenVactors[n + 2]) + 1].ljust(20)}')
		print(f'         {redunCoor[redunCoor.index(eigenVactors[n + 3]) + 1].ljust(20)}', end='')
		print(f'{redunCoor[redunCoor.index(eigenVactors[n + 4]) + 1].ljust(20)}', end='')
		print(f'{redunCoor[redunCoor.index(eigenVactors[n + 5]) + 1].ljust(20)}')
		print(' ')
else:
	print("\n[SCF] No SCF data yet, check again after several minutes.\n")

if jobType == 'opt':
	for o in range(len(logFile)):
		if "-- Stationary point found" in logFile[o]:
			print("\n[OPT] Stationary point found.")
		elif "Normal termination of Gaussian" in logFile[o]:
			print("[OPT] Optmization was finished.")
		elif "Error termination" in logFile[o]:
			print("[ERROR] Error termination was found.")
			break

if jobType == 'optfreq':
	for r in range(len(logFile)):
		if "-- Stationary point found" in logFile[r]:
			print("\n[OPT] Stationary point found.")
			break
	ternimationCount = 0
	for p in range(len(logFile)):
		if "Normal termination of Gaussian" in logFile[p]:
			ternimationCount += 1
		elif "Error termination" in logFile[p]:
			print("[ERROR] Error termination was found.")
			break
	if ternimationCount == 2:
		print("[OPT+FREQ] Optimization and frequency analysis were finished.")
	elif ternimationCount == 1:
		print("[OPT+FREQ] Optimization was finished, frequency analysis is running.")

print()
