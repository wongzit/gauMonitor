# Module of gauMonitor
# for opt, opt+freq, freq
# Written by Zhe Wang, 2021-07-16

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
	eneFlag = '~'
	eneDiff = float(ene1) - float(ene2)
	if eneDiff < 0.00000:
		eneFlag = '+'
	elif eneDiff > 0.00000:
		eneFlag = '-'
	return eneFlag

logPath = sys.argv[1]
#logPath = '/Users/wangzhe/Desktop/std_sat_im_opt.log'
print(f"Reading output file from {logPath} ...\n")
with open(logPath, 'r') as output:
	logFile = output.readlines()

jobType = sys.argv[2]

if jobType == 'scan':
	scfStart = 0
	print("Optimization job has found, looking for SCF iterations data...\n")
	for k in range(len(logFile)):
		if 'Threshold  Converged?' in logFile[k]:
			scfStart = 1
			threshold1 = logFile[k + 1].split()[3]
			threshold2 = logFile[k + 2].split()[3]
			threshold3 = logFile[k + 3].split()[3]
			threshold4 = logFile[k + 4].split()[3]
			break
	if scfStart == 1:
		print("---------------------------------- OPT SCF ITERATIONS ----------------------------------")
		print("  Cycle    Max.Force    RMS.Force    Max.Displacement    RMS.Displacement    Converged?")
		print("----------------------------------------------------------------------------------------")
		print(f"     0      {threshold1}     {threshold2}        {threshold3}            {threshold4}        Threshold")
		convergeCount = 0
		for j in range(len(logFile)):
			if 'Threshold  Converged?' in logFile[j]:
				convergeCount += 1
				print(f"   {format(str(convergeCount).rjust(3))}      {logFile[j + 1].split()[2]}     \
{logFile[j + 2].split()[2]}        {logFile[j + 3].split()[2]}            {logFile[j + 4].split()[2]}           \
{conOrNot(logFile[j + 1].split()[4], logFile[j + 2].split()[4], logFile[j + 3].split()[4], logFile[j + 4].split()[4])}")
			if "Normal termination of Gaussian" in logFile[j]:
				break
		print("----------------------------------------------------------------------------------------\n")
	else:
		print("NO SCF DATA YET. Check again after several minutes.\n")

	if scfStart == 1:
		scfEnergy = []
		print("\n--------------------- ELECTRONIC ENERGY ---------------------")
		for l in range(len(logFile)):
			if 'SCF Done' in logFile[l]:
				scfEnergy.append(logFile[l].split()[4])
			if "Normal termination of Gaussian" in logFile[l]:
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

for o in range(len(logFile)):
	if "-- Stationary point found" in logFile[o]:
		print("\n[OPT] Stationary point found.")
	elif "Normal termination of Gaussian" in logFile[o]:
		print("[OPT] Optmization was finished.")
	elif "Error termination of Gaussian" in logFile[o]:
		print("[ERROR] Error termination was found.")

print()