import requests
from colorama import Fore
import time
import os

print("=============================================")
author = "Bg.Pateng"
print("Spesial Thanks To " + author)
telegram = "@bangpateng_group"
print("Telegram: " + telegram)
youtube = "Bang Pateng"
print("Youtube: " + youtube)
print("===========================================")
print('PERINGATAN : TIDAK UNTUK DI PERJUAL-BELIKAN')
print("===========================================\n")

time.sleep(1)

channel_id = input("Masukkan ID Channel: ")
delay = int(input("Set Delay Kirim Pesan (dalam detik): "))

time.sleep(1)
print("Silahkan Tunggu")
time.sleep(1)
print(".............")
time.sleep(5)

os.system('cls' if os.name == 'nt' else 'clear')

with open("pesan.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

index = 0  # Initialize index to start from the first line

while True:
    channel_id = channel_id.strip()

    payload = {
        'content': words[index].strip()
    }

    headers = {
        'Authorization': authorization
    }

    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
    print(Fore.WHITE + "Sent message: ")
    print(Fore.YELLOW + payload['content'])

    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

    time.sleep(delay)
    index = (index + 1) % len(words)  # Move to the next line, looping back to the start if needed
