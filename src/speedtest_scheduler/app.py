from datetime import datetime
from os.path import exists
import schedule
import subprocess
import re
import csv
import time

# path for stats file
path = 'stats.csv'

def run_speedtest():
  """Runs speedtest command, prints and returns results."""
  date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
  print(f'\n{date}\nStarting speedtest.')
  cmd = 'speedtest | grep "load:"'
  speedtest = subprocess.check_output(cmd, shell=True).decode('UTF-8').split('\n')
  reg = re.compile('\d+.\d\d')
  dl  = reg.search(speedtest[0]).group(0)
  ul  = reg.search(speedtest[1]).group(0)
  print(f'Results:\nDownload: {dl} Mbit\nUpload: {ul} Mbit\n')
  return [date, ul, dl]

def write_csv_header():
  """
  Writes header to a new csv file.
  Will overwrite path file if it exists.
  """
  with open(path, 'w') as fp:
    fieldnames = ['date', 'download', 'upload']
    writer = csv.DictWriter(fp, fieldnames=fieldnames)
    writer.writeheader()

def write_csv(date,dl,ul):
  """Appends data to csv file."""
  with open(path, 'a') as fp:
    writer = csv.writer(fp)
    writer.writerow([date,dl,ul])

def set_schedule():
  """
  Prompts for user input, sets appropriate schedule.\n
  0 = every __ minutes\n
  1 = every hour\n
  2 = set time of day\n
  Defaults to 2 if anything other than 0 or 1 is entered.
  """
  num = input("Select mode:\n0 = every __ minutes\n1 = every hour\n2 (default) = set time of day\n")
  if num == "0":
    set_time = int(input("How many minutes between runs?\n"))
    print(f'Set to run every {set_time} minutes.')
    schedule.every(set_time).minutes.do(run)
  elif num == "1":
    schedule.every().hour.do(run)
    print("Set to run once an hour.")
  else:
    set_time = input("What time should the daily test run?\nPlease enter a time in the form of 00:00.\n")
    schedule.every().day.at(set_time).do(run)
    print(f'Set to run at {set_time} every day.')
  return num

def run():
  """Runs speedtest and appends data to csv file."""
  stats = run_speedtest()
  write_csv(stats[0],stats[1],stats[2])

def main():
  num = set_schedule()
  if exists(path): # if csv file exists, prompt for overwrite
    overwrite = input("Overwrite previous stats file? (y/n)\n")
    if overwrite.lower() == "y" or overwrite.lower() == "yes":
      write_csv_header()
  else:
    write_csv_header()
  if num == "0" or num == "1":
    run()
  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
  main()