#!/usr/bin/env python

import yt_dlp

# ANSI Escape code
R = '\033[91m' # Red
G = '\033[92m' # Green
Y = '\033[93m' # Yellow
B = '\033[94m' # Blue
M = '\033[95m' # Magenta
C = '\033[96m' # Cyan
W = '\033[97m' # White
RS = '\033[0m'  # Reset to default color

def magma_title_style():
  print(f"""{R}
   ███╗   ███╗ █████╗  ██████╗ ███╗   ███╗ █████╗
   ████╗ ████║██╔══██╗██╔════╝ ████╗ ████║██╔══██╗ Z
   ██╔████╔██║███████║██║  ███╗██╔████╔██║███████║ A
   ██║╚██╔╝██║██╔══██║██║   ██║██║╚██╔╝██║██╔══██║ X
   ██║ ╚═╝ ██║██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║ Py
   ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝""")


def download_audio(url):

  ydl_opts = {
    'format' : 'bestaudio/best',
    'postproccesors' : [{
      'key' : 'FFmpegExtractAudio',
      'preferredcodec' : 'mp3',
      'preferredquality' : '192',
    }],
    'outtmpl' : 'storage/dcim/%(title)s.%(ext)s',
  }
  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
  except DownloadError as e:
    print(f"Error downloading {url}: {str(e)}")

def main():
  magma_title_style()
  print(f'\n{G}YouTube Downloader with {R}Python')
  try :
    url = input(f'{G}[{W}+{G}] {Y}Enter the URL of YouTube Video: {RS}')
    while not url :
      url = input(f'{G}[{W}+{G}] {Y}Enter the URL of YouTube Video: {RS}')
    
    verify = input(f'{G}[{W}+{G}] {Y}Enter [ {C}Y{Y} ] to download : {RS}')
    if verify.lower() == 'y':
      download_audio(url)
      print(f'\n{W}Download Successful!\n')
    else :
      print(f'\n{W}Failed processing program!\n')
  except Exception as err:
    print(err)

if __name__ == '__main__' :
  main()
