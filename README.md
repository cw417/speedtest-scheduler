# Speedtest Scheduler
Scheduler for speedtest-cli

## Table of Contents
1. About
2. Getting Started
    1. Prerequisites
    2. Installing
3. How It Works

## About
Speedtest Scheduler is a program written in python that runs the speedtest-cli application at regular intervals set by the user to report network speed stats.


## Getting Started
### Prerequisites
- Linux-based operating system
- speedtest-cli
- Python 3.6+
- Python dependencies:
  - schedule

### Installing
1) Clone the github repository: `https://github.com/cw417/speedtest-scheduler`
2) Install speedtest-cli:
   - Ubuntu/Debian: `sudo apt-get install speedtest`
   - Fedora/RHEL: `sudo yum install speedtest`
   - Arch/Manjaro: `sudo pacman -S speedtest-cli`
3) Install python dependencies: `pip install schedule`
4) Edit file to set speedtest interval:
   - Use text editor of choice (nano, vim, gedit, pycharm, etc...) to open `speedtest_scheduler.py`
   - Navigate to commented out section near bottom of file, and uncomment/set your desired interval
   - Save the edited file and exit
5) Run speedtest-scheduler: `python speedtest_scheduler.py`
  
## How It Works
Speedtest-scheduler uses the speedtest application that interfaces with speedtest.net to test your current download and upload speeds at an interval set by the user, and writes these values to a CSV file for easy monitoring. The interval set by the user can be a set number of minutes or hours, or it can be set up to run every day at a specified time.