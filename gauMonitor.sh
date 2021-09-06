#! /bin/bash

echo ""
echo "                      *      g a u M o n i t o r      *                           "
echo ""
echo "                   --- A Gaussian jobs monitor package ---                        "
echo "                    - Program Version: 2.3.1 // RELEASE -                          "
echo ""
echo "             -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-                  "
echo "                  Developed by Zhe Wang (github.com/wongzit)                      "
echo "                     [Homepage] https://wongzit.github.io                         "
echo "                           Last update: 2021-09-05                                "
echo "             -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-                  "
echo ""

# Specify the gauMonitor path at following
GM_DIR='/home/hpc/wang/gauMonitor'

if [ ! $1 ]; then
	echo ""
	echo "[Useage] gaumonitor Gaussian_out.log"
	echo ""
	echo "         Support optimization and frequency analysis (opt/freq/opt+freq), IRC, and "
	echo "         scan (opt=modredundant) jobs."
	echo "         For more information, please refer to following website:"
	echo "                (1) https://github.com/wongzit/gauMonitor"
	echo "                (2) https://wongzit.github.io/program"
	echo ""
else
	jobtype=$(python3 $GM_DIR/jobType.py $1)
fi

#echo $jobtype

if [ ! $1 ]; then
	echo ""
else
	if [ $jobtype = "unknown" ]; then
		echo Unsupported job type.
	elif [ $jobtype = "opt" ]; then
		python3 $GM_DIR/gauMonitor.opt.py $1 opt
	elif [ $jobtype = "optfreq" ]; then
		python3 $GM_DIR/gauMonitor.opt.py $1 optfreq
	elif [ $jobtype = "freq" ]; then
		python3 $GM_DIR/gauMonitor.opt.py $1 freq
	elif [ $jobtype = "optts" ]; then
#		python3 $GM_DIR/gauMonitor.opt.py $1 opt
		python3 $GM_DIR/gauMonitor.ts.py $1 opt
	elif [ $jobtype = "optfreqts" ]; then
#		python3 $GM_DIR/gauMonitor.opt.py $1 optfreq
		python3 $GM_DIR/gauMonitor.ts.py $1 optfreq
	elif [ $jobtype = "scan" ]; then
		python3 $GM_DIR/gauMonitor.scan.py $1
	elif [ $jobtype = "irc" ]; then
		python3 $GM_DIR/gauMonitor.irc.py $1
	fi
fi

echo --- Termination of gauMonitor ---
echo ""