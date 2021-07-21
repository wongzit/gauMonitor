# Job-type module for gauMonitor
# Program version 2.0.0
# Last update: 2021-07-22

import sys

logPath = sys.argv[1]
#logPath = '/Users/wangzhe/Desktop/s08_cis_ts_qst3.log'
#logPath = '/Users/tetsu/Desktop/ts_test.log'

with open(logPath, 'r') as output:
	logFile = output.readlines()

for i in range(len(logFile)):
	if '------' in logFile[i] and '#' in logFile[i + 1]:
		routeLine = logFile[i + 1].strip().lower()
		if '------' not in logFile[i + 2]:
			routeLine = logFile[i + 1].strip().lower() + logFile[i + 2].strip().lower()
		break

if 'opt' in routeLine:
	if 'freq' in routeLine:
		jobType = 'optfreq'
	elif 'modredundant' in routeLine:
		jobType = 'scan'
	else:
		jobType = 'opt'
elif 'freq' in routeLine:
	jobType = 'freq'
elif 'irc' in routeLine:
	jobType = 'irc'
else:
	jobType = 'unknown'

if jobType == 'opt' or jobType == 'optfreq':
	routeWords = routeLine.split()
	for routeWord in routeWords:
		if 'opt' in routeWord:
			if 'qst' in routeWord or 'ts' in routeWord:
				jobType += 'ts'

print(jobType)