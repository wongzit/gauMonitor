# gauMonitor
![](logo.png)
Developed by [Zhe Wang](https://wongzit.github.io)

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
Check the user document:
```
gaumonitor -h
```

## Dependence
Python 3.2+, Bash shell

## Development environment
Python 3.9.6, Bash shell on macOS 11.4

## Update History
### v3.0.0 (2021-09-12)
1. Updated userinterface for SCF iteration section and energy section.
2. Now the directions (forward and reverse) will be displayed for IRC jobs.
3. Electronic energies of stationary points for SCAN calculations would be summarized in a new table.
4. Document has been added, use command `guamonitor -h` to check the user document.
5. Add supporting for calculations using `counterpoise` or `counter` keywords.
6. Improved stability.

### v2.3.0 (2021-07-25)
1. Bug fixed.

### v2.1.0 (2021-07-22)
1. Specify the gauMonitor path by inputting once.
2. Improved informations of transition states.

### v1.0.0 (2021-07-17)
1. IRC module is available now.
2. Modified the job type specification script.
