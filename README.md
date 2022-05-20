# CLI Pomodoro Timer

An application for time management and productivity utilizing the Pomodoro Technique. This program is a simple Python script that runs a timer on the command line. It does two things:

## 1) Start a pomodoro timer

Pomodoro mode is on by default. Simply call the command:
```bash
pomodoro
```


## 2) Set a countdown timer:
```bash
python pomodoro.py <--timer|-t> [-h][-m][-s] <HOUR|MINUTES|SECONDS>
```
ex. Setting a timer for 1 hour and 30 minutes:
```bash
python pomodoro.py t -h 1 -m 30
```

An alarm will ring when the time is up.

## Installation for Linux systems

Run this command: 
```bash
sudo python3 install.py
```

## For Windows

Run as Administrator:
```bash
python3 install.py
```

Restart computer (needed for adding pomodoro to PATH variable)

## Dependencies
* [pygame](https://pygame.org/wiki/GettingStarted)
