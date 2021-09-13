# gauMonitor module SCAN
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
#logPath = '/Users/wangzhe/Desktop/Ant_F_CH_scan.log'
#print(f"Reading output file from {logPath} ...\n")
with open(logPath, 'r') as output:
	logFile = output.readlines()

scfStart = 0
for k in range(len(logFile)):
	if 'Threshold  Converged?' in logFile[k]:
		scfStart = 1
		threshold1 = logFile[k + 1].split()[3]
		threshold2 = logFile[k + 2].split()[3]
		threshold3 = logFile[k + 3].split()[3]
		threshold4 = logFile[k + 4].split()[3]
		break
if scfStart == 1:
	print("\n# SCF ITERATIONS\n- Summary of SCF Iterations:\n")
	print("  Cycle    Max.Force     RMS.Force       Max.DP        RMS.DP    Converged?")
	print("-----------------------------------------------------------------------------")
	print(f"           ({threshold1})    ({threshold2})    ({threshold3})    ({threshold4})  Threshold")
	convergeCount = 0
	staPot = 0
	for j in range(len(logFile)):
		if 'Threshold  Converged?' in logFile[j]:
			convergeCount += 1
			print(f"   {format(str(convergeCount).rjust(3))}      {logFile[j + 1].split()[2]}      \
{logFile[j + 2].split()[2]}      {logFile[j + 3].split()[2]}      {logFile[j + 4].split()[2]}      \
{conOrNot(logFile[j + 1].split()[4], logFile[j + 2].split()[4], logFile[j + 3].split()[4], logFile[j + 4].split()[4])}")
		elif "-- Stationary point found" in logFile[j]:
			print("                         --- SCAN STEP FINISHED ---")
		elif "Normal termination of Gaussian" in logFile[j]:
			break
	print("-----------------------------------------------------------------------------\n")
else:
	print("\n[SCF] No SCF data yet, check again after several minutes.\n")

if scfStart == 1:
	scfEnergy = []
	scfCount = 0
	staNo = []
	print("\n- Summary of electronic energy:\n")
	for l in range(len(logFile)):
		if 'SCF Done' in logFile[l]:
			scfEnergy.append(logFile[l].split()[4])
			scfCount += 1
		elif '-- Stationary point found' in logFile[l]:
			staNo.append(scfCount)
		elif 'Normal termination of Gaussian' in logFile[l]:
			break
	print("  Cycle      E (Hartree)       E.rel (kcal/mol)     Delta-E")
	print("-------------------------------------------------------------")
	if len(scfEnergy) == 1:
		print(f"    1      {scfEnergy[0]}            0.000000")
	elif len(scfEnergy) > 1:
		print(f"    1      {scfEnergy[0]}            0.000000")
		for m in range(1, len(scfEnergy)):
			print(f"  {str(m + 1).rjust(3)}      {scfEnergy[m]}        {str(format(((float(scfEnergy[m]) - float(scfEnergy[0])) * 627.51), '.6f')).rjust(12)}          {eneComp(scfEnergy[m - 1], scfEnergy[m])}")
	print("-------------------------------------------------------------\n")

if staNo:
	print("\n# SCAN STEP\n- Summary of electronic energies for stationary points:\n")
	print("  Steps      E (Hartree)       E.rel (kcal/mol)     Delta-E")
	print("-------------------------------------------------------------")
	for p in range(len(staNo)):
		print(f"  {str(p + 1).rjust(3)}      {scfEnergy[staNo[p] - 1]}        {str(format(((float(scfEnergy[staNo[p] - 1]) - float(scfEnergy[staNo[0] - 1])) * 627.51), '.6f')).rjust(12)}", end='')
		if p == 0:
			print(" ")
		else:
			print(f"          {eneComp(scfEnergy[staNo[p - 1] - 1], scfEnergy[staNo[p] - 1])}")
	print("-------------------------------------------------------------\n")

for o in range(len(logFile)):
	if "Normal termination of Gaussian" in logFile[o]:
		print("[OPT=MODREDUNDANT] Calculation was finished.")
	elif "Error termination" in logFile[o]:
		print("[ERROR] Error termination was found.")
		break

print()