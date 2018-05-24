# CLI Pomodoro Timer

Python script to run a CLI timer that does two things:

## 1) Start a pomodoro timer

Pomodoro mode is on by default. Simply run the script:
```bash
python pomodoro.py
```


## 2) Set a countdown timer:
```bash
python pomodoro.py <--timer|-t> [-h][-m][-s] <HOUR|MINUTES|SECONDS>
```
ex. Setting a timer for 1 hour and 30 minutes:
```bash
python pomodoro.py t -h 1 -m 30
```

## Installation for Linux systems

Run this command: 
```bash
sudo python3 install.py
```
## Dependencies
* [pygame](https://pygame.org/wiki/GettingStarted)
