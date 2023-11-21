import socket

class Connection:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()
    
    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.HOST, self.PORT))
    
    def get_variable(self, name):
        self.socket.send(f"GET${name}".encode())
        data = self.socket.recv(1024).decode()
        self.connect()
        return eval(data)

    def set_variable(self, name, value):
        self.socket.send(f"SET${name}${repr(value)}".encode())
        self.connect()
    
    def save(self):
        self.socket.send(f"SAVE".encode())
        self.connect()