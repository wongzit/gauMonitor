# gauMonitor module JOBTYPEFINDER
# Program version: 3.0.0
# Update at 2021-09-12

import sys

logPath = sys.argv[1]
#logPath = '/Users/wangzhe/Desktop/s08_cis_ts_qst3.log'
#logPath = '/Users/wangzhe/Desktop/ts_test.log'

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

if 'counter' in routeLine or 'counterpoise' in routeLine:
	print(jobType + 'bsse')
else:
	print(jobType)
