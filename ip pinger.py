import requests
from os import system
from colorama import Fore

def renderMenu():
    print(f"{Fore.CYAN}   _____  _____   _____ _                       ")
    print("  / ____|/ ____| |  __ (_)                      ")
    print(" | (___ | |      | |__) | _ __   __ _  ___ _ __ ")
    print("  \___ \| |      |  ___/ | '_ \ / _` |/ _ \ '__|")
    print(f"{Fore.BLUE}  ____) | |____  | |   | | | | | (_| |  __/ |   ")
    print(" |_____/ \_____| |_|   |_|_| |_|\__, |\___|_|   ")
    print("                                 __/ |          ")
    print(f"                                |___/          {Fore.RESET}")


def clear():
    system("cls")

while True:
    clear()
    system("title SCPinger Made by SCPrograms")
    renderMenu()
    print("[1] Start Pinger")
    print("[2] Exit")

    opt = input("Option: ")
    if opt == "1":
        clear()
        system("title Pinger Started Press CNTRL + C TO EXIT BY ScPrograms")
        ip = input("IP: ")
        while True:
            try:
                r = requests.get(f"http://{ip}", timeout=5)
                if r.status_code == 200:
                    print(f"{Fore.GREEN}IP Online{Fore.RESET}")
            except requests.exceptions.RequestException:
                print(f"{Fore.RED}IP IS OFFLINE {Fore.RESET}")
    if opt == "2":
        exit()
