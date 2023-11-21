import socket, json

class Database:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.collection = {

        }

    def connect(self):
        try:
            self.socket.bind((self.HOST, self.PORT))
            self.socket.listen()
        except:
            pass
    
    def get_operation(self):
        c, addr = self.socket.accept()
        print(f"{addr} answered.")

        msg = c.recv(1024).decode().split("$")

        if msg[0] == "SET": self.collection[msg[1]] = eval(msg[2])
        elif msg[0] == "GET":
            if msg[1] in self.collection: c.send(repr(self.collection[msg[1]]).encode())
        elif msg[0] == "SAVE":
            with open("infs.json", "w") as f: json.dump(self.collection, f)
        
        print("Responded.")
        c.close()

HOST = "localhost"
PORT = 3453

db = Database(HOST, PORT)
db.connect()

while True:
    db.get_operation()