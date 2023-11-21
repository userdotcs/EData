import serverDC

HOST = "localhost"
PORT = 3453

conn = serverDC.Connection(HOST, PORT)

conn.set_variable("variable", 2)
print(conn.get_variable("variable"))