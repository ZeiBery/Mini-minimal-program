from collections import deque
import re
from bs4 import BeautifulSoup
import requests
import urllib.parse
from colorama import Fore, init, Style

# autoreset color
init(autoreset=True)
# Input URL target
target_url = input(f'\n{Fore.RED}[-] {Fore.CYAN + Style.BRIGHT}Enter target url: {Fore.WHITE}').strip()
# Limit batas scan
limit = int(input(f'{Fore.RED}[-] {Fore.CYAN + Style.BRIGHT}Enter Limit for scrapping: {Fore.RED}'))
# Struktur data untuk menyimpan URL dan email
urls = deque([target_url])
scrapped_urls = set()
emails = set()
count_scan = 0

# Regex untuk mencari email
email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
print()
try:
    while urls:
        count_scan += 1
        if count_scan > limit:  # Batas maksimal scanning
            break
        
        url = urls.popleft()
        scrapped_urls.add(url)
        
        # Mendapatkan base URL
        parts = urllib.parse.urlsplit(url)
        base_url = f"{parts.scheme}://{parts.netloc}"
        path = url[:url.rfind('/')+1] if '/' in parts.path else url
        
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN + Style.BRIGHT}Proccessing: {Fore.WHITE}{url}")

        try:
            response = requests.get(url, timeout=5)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.Timeout):
            continue  # Lewati URL yang tidak valid
        
        # Mencari email dalam halaman
        new_emails = set(re.findall(email_regex, response.text, re.I))
        emails.update(new_emails)
        
        # Parsing halaman dengan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Mencari link dalam halaman
        for anchor in soup.find_all('a', href=True):
            link = anchor['href']
            
            if link.startswith('/'):
                link = base_url + link  # Menangani URL relatif
            elif not link.startswith('http'):
                link = urllib.parse.urljoin(path, link)  # Menangani URL yang tidak lengkap
            
            # Tambahkan URL ke antrian jika belum diproses
            if link not in urls and link not in scrapped_urls:
                urls.append(link)

except KeyboardInterrupt:
    print("\n[-] Proses dihentikan oleh pengguna.")

# Menampilkan hasil email yang ditemukan
print(f'\n{Fore.WHITE + Style.BRIGHT}Proccess Completed!')
print(f"\n{Fore.RED}[+] {Fore.CYAN + Style.BRIGHT}Emails founded:")
for mail in emails:
    print(f'{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] {Fore.YELLOW + Style.BRIGHT}{mail}')
