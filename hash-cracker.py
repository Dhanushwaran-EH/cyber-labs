# hash-cracker.py
import hashlib

hash_input = input("Enter SHA-256 hash: ")
wordlist = input("Enter path to wordlist (e.g., wordlist.txt): ")

try:
    with open(wordlist, "r") as file:
        for word in file:
            word = word.strip()
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == hash_input:
                print(f"[+] Password found: {word}")
                break
        else:
            print("[-] Password not found in wordlist.")
except FileNotFoundError:
    print("[-] Wordlist file not found.")
