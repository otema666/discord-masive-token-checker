from colorama import Fore, init, Style

import requests
init()

def TokenChecker(token, n):
    init(convert=True) # makes console support ANSI escape color codes
    print(f'{n}. Token: {Fore.GREEN}{token}{Fore.RESET}')       
    # print("Comprobando existencia de la cuenta", end="")
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    if res.status_code == 200: # code 200 if valid
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        print(f'{Fore.GREEN}[√]{Fore.RESET}¡CUENTA ENCONTRADA!: {Fore.BLUE}{user_name}')
        input("ENTER PARA CONTINUAR")
    elif res.status_code == 401: # code 401 if invalid
        print(f'{Fore.RED}[-] {Fore.RESET}No válido')
    else:
        print(f'{Fore.RED}[-] {Fore.RESET}No se pudo comprobar en tola data base')

def espacio():
    for a in range(24):
            print(Fore.GREEN + "-" + Style.RESET_ALL, end="", flush=True)
            print(Fore.RED + "-" + Style.RESET_ALL, end="", flush=True)  
            print(Fore.BLUE + "-" + Style.RESET_ALL, end="", flush=True)
            print(Fore.YELLOW + "-" + Style.RESET_ALL, end="", flush=True)
            print(Fore.MAGENTA + "-" + Style.RESET_ALL, end="", flush=True)

# Abre el archivo en modo lectura
archivo = open("tokenList.txt", "r")

num = 0
for token in archivo:
    num += 1
    token = token.rstrip()
    espacio()
    print()
    TokenChecker(token, num)
    print()
    




archivo.close()
