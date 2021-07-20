#! /bin/bash

echo ""
echo "                      *      g a u M o n i t o r      *                           "
echo ""
echo "                   --- A Gaussian jobs monitor package ---                        "
echo "                    - Program Version: 1.0.0 // RELEASE -                          "
echo ""
echo "             -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-                  "
echo "                  Developed by Zhe Wang (github.com/wongzit)                      "
echo "                         [Homepage] www.wangzhe95.net                             "
echo "                           Last update: 2021-07-17                                "
echo "             -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-                  "
echo ""

if [ ! $1 ]; then
	echo ""
	echo "[Useage] gaumonitor Gaussian_out.log"
	echo ""
	echo "         Support optimization and frequency analysis (opt/freq/opt+freq), IRC, and "
	echo "         scan (opt=modredundant) jobs."
	echo "         For more information, please refer to following website:"
	echo "                (1) https://github.com/wongzit/gauMonitor"
	echo "                (2) https://www.wangzhe95.net/program-gaumonitor"
	echo ""
else
	jobtype=$(python3 /home/hpc/wang/gauMonitor/jobType.py $1)
fi

#echo $jobtype

if [ ! $1 ]; then
	echo ""
else
	if [ $jobtype = "unknown" ]; then
		echo Unsupported job type.
	elif [ $jobtype = "opt" ]; then
		python3 /home/hpc/wang/gauMonitor/gauMonitor.opt.py $1 $jobtype
	elif [ $jobtype = "optfreq" ]; then
		python3 /home/hpc/wang/gauMonitor/gauMonitor.opt.py $1 $jobtype
	elif [ $jobtype = "freq" ]; then
		python3 /home/hpc/wang/gauMonitor/gauMonitor.opt.py $1 $jobtype
	elif [ $jobtype = "scan" ]; then
		python3 /home/hpc/wang/gauMonitor/gauMonitor.scan.py $1
	elif [ $jobtype = "irc" ]; then
		python3 /home/hpc/wang/gauMonitor/gauMonitor.irc.py $1
	fi
fi

echo --- Termination of gauMonitor ---
echo ""