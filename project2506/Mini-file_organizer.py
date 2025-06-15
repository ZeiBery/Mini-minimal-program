#!/bin/env python

import os
import shutil
import time
import sys

# Colors
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
magenta = '\033[95m'
cyan = '\033[96m'
white = '\033[97m'
reset = '\033[0m'

# Catgories for extention
file_categories: dict[str] = {
  'Video' : ['.mp4', '.webm'],
  'Audio' : ['.mp3', '.wav'],
  'Picture' : ['.jpg', '.png', '.jpeg', '.JPG'],
  'WebDevelopment' : ['.html', '.css'],
  'Programming' : ['.py', '.js', '.sh', '.c', '.cpp', '.php', 'java'],
  'Document' : ['.docx', '.pdf', '.pptx', '.txt', '.xlsx', '.xls'],
  'Archive' : ['.zip', '.7z','.tar','.tar.gz','.xz','.tar.xz'],
}

# Making the decoration
def run(text, delay=0.1):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()  # new line

# to check if the directory has been Created
def dir_check():
  for key in file_categories.keys():
    if not os.path.exists(f'{os.getcwd()}/{key}'):
      os.mkdir(key) # Create the directory

# The numbers of files in directory
def file_check():
  pwd = os.getcwd() # current working directory
  files = [] # Inisial
  for file in os.listdir(pwd):
    if os.path.isfile(os.path.join(pwd, file)):
      files.append(file)

  # return the numbers of files
  return files

# Mode 1: destination in current directory
def file_moved():
  moved = 0 # count of move
  for f in file_check():
    for d, ext in file_categories.items():
      if f.endswith(tuple(ext)):
        shutil.move(f, d)

        moved += 1
  print(f'\n{yellow}Announcement:\n{cyan}{moved} {green}items have been moves to the destination directory.\n')

# main function
def main():
  run(f'{yellow}Running the program.. {cyan}Please wait.', 0.09)
  dir_check()
  file_moved()
  print(f'{red}Succesfull!{reset}\n')

# Mode 2: with destination
def destination(source):
  moved = 0 # count of move
  target = '/data/data/com.termux/files/home/storage/shared'
  for f in source :
    for d, ext in file_categories.items():
      if f.endswith(tuple(ext)):
        shutil.move(f, f'{target}/{d}')

if __name__ == '__main__' :
  main()

# Happy coding 2025
# © May 3 2025 V.1.0
# © May 4 2025 V.1.1 Update Colors