import asyncio
import re
import uuid

from packages.models import Client
host = '5.5.5.1'
port = 14447

global CLIENTS
CLIENTS = {}

async def generateNewClient(writer,reader,username,addr):
    newclient = Client(writer,reader,username, addr)
    CLIENTS[uuid.uuid4()] = newclient
    print(CLIENTS)


async def joinEvent(writeradrr):
        for id in CLIENTS:
            writer = CLIENTS[id].writer
            servermessage = f"{CLIENTS[id].username} a rejoint la chatroom".encode("utf-8")
            writer.write(servermessage)
        return


async def leaveEvent(writeradrr):
    for id in CLIENTS:
        writer = CLIENTS[id].writer
        if CLIENTS[id].username == '':
            CLIENTS[id].username = CLIENTS[id].writer
        servermessage = f"{CLIENTS[id].username} a quitté la chatroom".encode("utf-8")
        writer.write(servermessage)
    return
    

async def sendAll(message, writeradrr):
    for id in CLIENTS:
        writer = CLIENTS[id].writer
        servermessage = f"{CLIENTS[id].user} : {message}".encode("utf-8")
        writer.write(servermessage)
    return

async def handle_packet(reader, writer):
    addr = writer.get_extra_info('peername')   
    while True:
        data = await reader.read(100)
        message = data.decode('utf-8')
        if not data:
            await asyncio.sleep(0.05)
        print(f"Message received from {addr[0]!r}:{addr[1]!r} :{message!r}")
        if data == b'': # Gestion de la déco relou le loup
            await leaveEvent(addr)
            writer.close()
            await writer.wait_closed()
            return
        if CLIENTS[id].username == '':
            if re.match(r'^[a-z0-9_-]{3,15}$', message):
                CLIENTS[id].username = message
                generateNewClient(writer,reader,message,addr)
                await joinEvent(addr)
        else:
            await sendAll(message, addr)
       
        await writer.drain()
        
    # Je laisse ça là ça peut toujours me servir
   

async def main():
    server = await asyncio.start_server(handle_packet, host, port)

    addr = server.sockets[0].getsockname()
    print(f"Serveur en écoute sur {addr}")

    async with server:
        await server.serve_forever()    


if __name__ == "__main__":
    asyncio.run(main())