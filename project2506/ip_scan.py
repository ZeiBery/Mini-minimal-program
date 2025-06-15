#!/usr/bin/env python

# colors
RED = "\033[91m"
G = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
W = "\033[97m"
cyan = "\033[96m"

# Title
def great():
  print(f"""{RED}
  █▀▀▄ █▀▀█ █▀▀█ █▀▄▀█ █▀▀ █▀▀▄ █▀▀█ █  █
  █  █ █  █ █  █ █ ▀ █ ▀▀█ █  █ █▄▄█ █▄▄█
  █▄▄▀ ▀▀▀▀ ▀▀▀▀ ▀   ▀ ▀▀▀ ▀▀▀  ▀  ▀ ▄▄▄█
  \t\t{RED}E: {YELLOW}Create by Zaini Harris
  """)

import socket
import sys
import time
import os

def loading_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Pindah ke baris baru

def scan_port(target, port):
    try:
        # Membuat socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout untuk koneksi

        # Mencoba koneksi ke target pada port tertentu
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"{G}[{W}+{G}] {YELLOW}Port {port} terbuka")
        sock.close()
    except Exception as e:
        print(f"{RED}Terjadi kesalahan: {e}")

# Scan beberapa port umum
common_ports = [21, 22, 23, 25, 53, 80, 443, 8080]
# common_ports = [x for x in range(1, 9000+1)]
def main():
    os.system("clear")
    great()

    # Input target dari user
    target = input(f"{G}Masukkan IP atau domain target: {RESET}")
    if not target :
        print('Invalid Domain')
    else :
        print(f"{G}Scanning target {RESET}{target}...\n")
        loading_effect(f"{G}[🔍] {YELLOW}Memulai proses scaning target...\n{RESET}", 0.09)

        for port in common_ports:
            scan_port(target, port)

if __name__ == '__main__':
    main()
