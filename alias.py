import requests
import time

# API prihlasovaci udaje
API_USER = "UZIVATELSKE_JMENO" #Uzivatelske jmeno na Wedosu, vetsinou email k prihlaseni 
API_PASSWORD = "API_HESlO" # API heslo nastavene v WAPI sekci
WEBHOSTING = "domeny.fun"  # domena na kterou bude koupeny hosting
IP_ADDRESS = "46.28.106.172"  # IP adresa hostingu (uz je vyplněna)

# nacteni seznamu domen prvni test.txt pro otestovani az pak pouzit domains.txt
with open("test.txt", "r") as file:
    domains = [line.strip() for line in file.readlines()]

for domain in domains:
    print(f"Pridavam alias: {domain}")

    alias_payload = {
        "request": {
            "user": API_USER,
            "password": API_PASSWORD,
            "command": "webhosting-add-alias",
            "data": {
                "webhosting": WEBHOSTING,
                "domain": domain,
                "dns": "on",  # Automaticky nastavit DNS
            }
        }
    }
    response = requests.post("https://api.wedos.com/wapi/json", json=alias_payload)
    print("Alias přidán:", response.json())

    # Pauza mezi požadavky, aby Wedos API neblokovalo
    time.sleep(1)

print("Vsechny domeny byly uspesne pridany a nakonfigurovany")
