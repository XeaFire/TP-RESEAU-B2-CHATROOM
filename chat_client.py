import socket
import sys
import asyncio
import aioconsole
import re

# On définit la destination de la connexion
host = 'localhost'  # IP du serveur
port = 14447           # Port choisi par le serveur
# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur



async def receive(reader,writer):
    while True:
        while True:
            data = await reader.read(1024)
            if data:
                print(data.decode())
            else:
                await asyncio.sleep(0.05)


async def clientinput(reader,writer):
    while True:
        print("Que veux tu envoyer au serveur ? ")
        clientmessage = await aioconsole.ainput()
        msg = clientmessage.encode("utf-8")
        writer.write(msg)
        await writer.drain()

async def main():
    try :
        reader, writer = await asyncio.open_connection(host, port)
    except socket.error as msg:
        print(f"Erreur de connexion avec le serveur : {msg}")
        sys.exit(1)

    # note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()

    print(f"Connecté avec succès au serveur {host} sur le port {port}")

    
    while True:
        print("Veuillez choisir un pseudo:")
        username = input()
        print(username)
        if re.match(r'^[a-z0-9_-]{3,15}$', username):
            break
        else:
            print("Pseudo invalide veuillez choisir un pseudo de 3 à 16 characteres") 
            continue
    
    msg = username.encode("utf-8")
    writer.write(msg)
    await writer.drain()

    # Gestion des Tasks héhé pouet pouet je suis un clown
    tasks = [receive(reader,writer) , clientinput(reader,writer)]
    await asyncio.gather(*tasks)
    

asyncio.run(main())