#! /bin/bash

echo ""
echo "                   +++++++++++++++++++++++++++++++++++++++++++++++++"
echo "                   +                                               +"
echo "                   +                 gauMonitor v0.1               +"
echo "                   +                                               +"
echo "                   + ------------------ Zhe Wang ----------------- +"
echo "                   +                                               +"
echo "                   +           https://www.wangzhe95.net           +"
echo "                   +                                               +"
echo "                   +++++++++++++++++++++++++++++++++++++++++++++++++"
echo ""

jobtype=$(python3 /home/hpc/wang/gauMonitor/jobType.py $1)

if [ $jobtype = "unknown" ]; then
	echo Unsupported job type.
elif [ $jobtype = "opt" ]; then
	python3 /home/hpc/wang/gauMonitor/gauMonitor.opt.py $1 $jobtype
elif [ $jobtype = "optfreq" ]; then
	python3 /home/hpc/wang/gauMonitor/gauMonitor.opt.py $1 $jobtype
elif [ $jobtype = "freq" ]; then
	python3 /home/hpc/wang/gauMonitor/gauMonitor.opt.py $1 $jobtype
elif [ $jobtype = "scan" ]; then
	python3 /home/hpc/wang/gauMonitor/gauMonitor.scan.py $1 $jobtype
fi

echo --- Termination of gauMonitor ---
echo