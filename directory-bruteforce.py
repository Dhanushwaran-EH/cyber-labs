# directory-bruteforce.py
import requests

url = input("Enter target URL (e.g., http://example.com/): ")
wordlist = input("Enter path to wordlist (e.g., dirs.txt): ")

try:
    with open(wordlist, "r") as file:
        for word in file:
            path = word.strip()
            full_url = url + path
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"[+] Found: {full_url}")
except FileNotFoundError:
    print("[-] Wordlist not found.")
except requests.exceptions.RequestException:
    print("[-] Error accessing target.")
