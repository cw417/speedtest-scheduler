from datetime import datetime
import schedule
import subprocess
import re
import csv
import time

def dl():
  # Get the download speed
  cmd = 'speedtest | grep Download'
  speedtest = str(subprocess.check_output(cmd, shell=True))
  reg = re.compile('\d*.\d\d')
  match  = reg.search(speedtest).group(0)
  return match

def ul():
  # Get the upload speed
  cmd = 'speedtest | grep Upload'
  speedtest = str(subprocess.check_output(cmd, shell=True))  
  reg = re.compile('\d*.\d\d')
  match  = reg.search(speedtest).group(0)
  return match

def formatted():
  # Run tests and format output
  date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  print(f'\n{date}\nStarting speedtest.')
  down = dl()
  up = ul()
  print('Speedtest done.')
  return [date, down, up, f'Results:\nDownload: {down} Mbit\nUpload: {up} Mbit']

def write_csv_header():
  with open('speedtest_stats.csv', 'w') as fp:
    fieldnames = ['date', 'download', 'upload']
    writer = csv.DictWriter(fp, fieldnames=fieldnames)
    writer.writeheader()

def write_csv(date,dl,ul):
  with open('speedtest_stats.csv', 'a') as fp:
    writer = csv.writer(fp)
    writer.writerow([date,dl,ul])

def run():
  stats = formatted()
  write_csv(stats[0],stats[1],stats[2])
  print(stats[3])

# Write CSV Header
write_csv_header()

# Perform run at set interval
# Uncomment and replace X to run every X minutes
# schedule.every(X).minutes.do(run) 
# Uncomment to run once an hour
# schedule.every().hour.do(run)
# Uncomment and replace X with 00:00-style time to run at set time every day 
# schedule.every().day.at('X').do(run)

while True:
  schedule.run_pending()
  time.sleep(1)