# Module of gauMonitor
# for IRC
# Written by Zhe Wang, 2021-07-17

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
#logPath = '/Users/wangzhe/Desktop/2a_2ndconf_d11_cleavege_scan.log'
#print(f"Reading output file from {logPath} ...\n")
with open(logPath, 'r') as output:
	logFile = output.readlines()

#jobType = sys.argv[2]

scfStart = 0
for k in range(len(logFile)):
	if 'SCF Done' in logFile[k]:
		scfStart = 1
		break

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
else:
	print("NO SCF DATA YET. Check again after several minutes.\n")

for o in range(len(logFile)):
	if "Normal termination of Gaussian" in logFile[o]:
		print("[IRC] Calculation was finished.")
	elif "Error termination" in logFile[o]:
		print("[ERROR] Error termination was found.")
		break

print()