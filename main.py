from colorama import Fore, init, Style
import requests

init()
token_success = []
token_failure = []
def TokenChecker(token, n):
    init(convert=True) # makes console support ANSI escape color codes
    print(f'{n}. Token: {Fore.GREEN}{token}{Fore.RESET}')
    print()
    # print("Comprobando existencia de la cuenta", end="")
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    if res.status_code == 200: # code 200 if valid
        token_success.append(token)
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        print(f'{Fore.GREEN}[√]{Fore.RESET}¡CUENTA ENCONTRADA!: {Fore.BLUE}{user_name}')
        # input("ENTER PARA CONTINUAR")
    elif res.status_code == 401: # code 401 if invalid
        token_failure.append(token)
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

def numTokens():
    n = 0
    for num in archivo:
        n += 1
    return n
         






# Abre el archivo en modo lectura
archivo = open("tokenList.txt", "r")
numero_de_tokens = numTokens()
print(f'{Fore.LIGHTWHITE_EX}Número de tokens en el archivo: {Fore.GREEN}{numero_de_tokens}{Fore.RESET}')
print(f'Presiona {Fore.GREEN}ENTER{Fore.RESET} para continuar')
input()
archivo.seek(0)
num = 0
for token in archivo:
    num += 1
    token = token.rstrip()
    espacio()
    print()
    TokenChecker(token, num)

archivo.close()

espacio()
espacio()
print(f'                                                 {Fore.BLUE}PROGRAMA FINALIZADO{Fore.RESET}')
print()
print(f"* TOKENS INVÁLIDOS: {Fore.RED}{len(token_failure)}{Fore.RESET}.")
print(f"* TOKENS VÁLIDOS: {Fore.GREEN}{len(token_success)}{Fore.RESET}.")
if len(token_success) > 0:
    print(f"Presiona {Fore.GREEN}ENTER {Fore.RESET}para ver la lista de tokens válidos.")
    input()
    print()
    for element in token_success:
        print(f"--> {element}")
espacio()
print()