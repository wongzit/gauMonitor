import sys

logPath = sys.argv[1]
#logPath = '/Users/wangzhe/Desktop/std_sat_im_opt.log'

with open(logPath, 'r') as output:
	logFile = output.readlines()

for i in range(len(logFile)):
	if '------' in logFile[i] and '#' in logFile[i + 1]:
		routeLine = logFile[i + 1].strip().lower()
		if '------' not in logFile[i + 2]:
			routeLine = logFile[i + 1].strip().lower() + ' ' + logFile[i + 2].strip().lower()
		break

#print(routeLine)

if 'opt' in routeLine:
	if 'freq' in routeLine:
		jobType = 'optfreq'
	elif 'freq' not in routeLine and 'stable' not in routeLine:
		jobType = 'opt'
	elif 'modredundant' in routeLine:
		jobType = 'scan'
elif 'freq' in routeLine and 'opt' not in routeLine:
	jobType = 'freq'
elif 'irc' in routeLine:
	jobType = 'irc'
else:
	jobType = 'unknown'

print(jobType)