# gauMonitor
![](logo.png)
Developed by [Zhe Wang](https://www.wangzhe95.net)


Version: v1.0.0 stable release

*gauMonitor* is a program package for monitoring the Gaussian calculation jobs. It supports the optimization (opt), 
frequency analysis (freq/opt+freq), relaxed scan (opt=modredundant) and IRC jobs.

## Usage
Modify the *gauMonitor* path in the *gauMonitor.sh* script.
*gauMonitor* is written in Bash shell and Python script. It is designed for HPC so only Linux and macOS are supported.
Add following command to .bashrc file:
```
alias gaumonitor=/path/to/gauMonitor/foler/gauMonitor.sh
```
and running *gauMonitor* with:
```
gaumonitor [Gaussian_out.log]
```

## Dependence
Python 3.2+, Bash shell

## Development environment
Python 3.9.6, Bash shell on macOS 11.4

## Update History
### v2.1.0 (2021-07-22)
1. Specify the gauMonitor path by inputting once.
2. Improved informations of transition states.

### v1.0.0 (2021-07-17)
1. IRC module is available now.
2. Modified the job type specification script.
