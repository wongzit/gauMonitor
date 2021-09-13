#! /bin/bash

echo ""
echo "                      *      g a u M o n i t o r      *                           "
echo ""
echo "                   --- A Gaussian jobs monitor package ---                        "
echo "                         - Version 3.0.0 / RELEASE -                              "
echo ""
echo "             -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-                  "
echo "                 Developed by Zhe Wang, Hiroshima University                      "
echo "                     [Homepage] https://wongzit.github.io                         "
echo "                           Last update: 2021-09-12                                "
echo "             -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-                  "
echo ""

# Specify the gauMonitor path at following
GM_DIR='/home/wangzhe/gauMonitor-3.0.0'

if [ ! $1 ]; then
	echo ""
	echo "         [Useage]  gaumonitor /path_to/gaussian_output.log"
	echo "      [Documents]  gaumonitor -h"
	echo ""
	echo "Support optimization and frequency analysis (opt/freq/opt+freq), IRC, and"
	echo "scan (opt=modredundant) jobs."
	echo "For more information, please refer to following website:"
	echo "       (1) https://github.com/wongzit/gauMonitor"
	echo "       (2) https://wongzit.github.io/program"
	echo ""
elif [ "$1" = "-h" ]; then
	python3 $GM_DIR/gauMonitor.help.py
else
	jobtype=$(python3 $GM_DIR/jobType.py $1)
fi

if [ ! $1 ]; then
	echo ""
elif [ "$1" != "-h" ]; then
	if [ $jobtype = "unknown" ]; then
		echo Unsupported job type.
	elif [ $jobtype = "opt" ]; then
		python3 $GM_DIR/gauMonitor.opt.py $1 opt
	elif [ $jobtype = "optfreq" ]; then
		python3 $GM_DIR/gauMonitor.opt.py $1 optfreq
	elif [ $jobtype = "freq" ]; then
		python3 $GM_DIR/gauMonitor.opt.py $1 freq
	elif [ $jobtype = "optbsse" ]; then
		python3 $GM_DIR/gauMonitor.opt.bsse.py $1 opt
	elif [ $jobtype = "optfreqbsse" ]; then
		python3 $GM_DIR/gauMonitor.opt.bsse.py $1 optfreq
	elif [ $jobtype = "freqbsse" ]; then
		python3 $GM_DIR/gauMonitor.opt.bsse.py $1 freq
	elif [ $jobtype = "optts" ]; then
		python3 $GM_DIR/gauMonitor.ts.py $1 opt
	elif [ $jobtype = "optfreqts" ]; then
		python3 $GM_DIR/gauMonitor.ts.py $1 optfreq
	elif [ $jobtype = "opttsbsse" ]; then
		python3 $GM_DIR/gauMonitor.ts.bsse.py $1 opt
	elif [ $jobtype = "optfreqtsbsse" ]; then
		python3 $GM_DIR/gauMonitor.ts.bsse.py $1 optfreq
	elif [ $jobtype = "scan" ]; then
		python3 $GM_DIR/gauMonitor.scan.py $1
	elif [ $jobtype = "irc" ]; then
		python3 $GM_DIR/gauMonitor.irc.py $1
	fi
fi

echo "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
echo ""
echo "         Termination of gauMonitor at `date`."
echo ""
echo "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
