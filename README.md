# speedtest-scheduler

Scheduler for speedtest-cli

## Table of Contents

1. About
2. Getting Started
    1. Prerequisites
    2. Installing
3. How It Works

## About

Uses `speedtest-cli` to test upload/download speed at set intervals.
Records the data in a csv file.

## Getting Started

### Prerequisites

- Linux-based operating system
- speedtest-cli
- Python 3.6+
- Python dependencies:
  - schedule

### Installing

1) Clone the github repository: `git clone https://github.com/cw417/speedtest-scheduler`
2) Install speedtest-cli:

   - Arch/Manjaro: `sudo pacman -S speedtest-cli`
3) Install python dependencies: `pip install schedule`
4) Edit file to set speedtest interval:
   - Use text editor of choice (nano, vim, gedit, pycharm, etc...) to open `speedtest_scheduler.py`
   - Navigate to commented out section near bottom of file, and uncomment/set your desired interval
   - Save the edited file and exit
5) Run speedtest-scheduler: `python speedtest_scheduler.py`
  
## How It Works

- uses the speedtest-cli application to test upload and download speed
- the interval set by the user
  - must be set inside the speedtest_scheduler.py file
  - default is every day at 04:00 AM
- data is written to speedtest_stats.csv
