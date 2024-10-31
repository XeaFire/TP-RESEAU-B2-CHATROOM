class Client:
    def __init__(self, writer, reader, username, addr):
        self.writer = writer
        self.username = username
        self.reader = reader
        self.connected = True
        self.address = addr