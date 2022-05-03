# speedtest-scheduler

Scheduler for speedtest-cli

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- [How It Works](#how-it-works)

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
   - Ubuntu: `sudo apt install speedtest-cli`
   - Arch/Manjaro: `sudo pacman -S speedtest-cli`
3) Install python dependencies: `pip install schedule`
4) Run speedtest-scheduler: `python3 app.py`
  
## How It Works

- uses the speedtest-cli application to test upload and download speed
- the interval set by the user
  - must be set inside the speedtest_scheduler.py file
  - default is every day at 04:00 AM
- data is written to speedtest_stats.csv
