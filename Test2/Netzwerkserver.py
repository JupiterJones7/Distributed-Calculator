import sys
from xmlrpc.server import SimpleXMLRPCServer

argumentList = sys.argv
hostAddress = '0.0.0.0'
port = 12345
server = SimpleXMLRPCServer((hostAddress, int(port)))

def test(x, y):
    Username = "Timi"
    Passwort = 12345
    if x == Username and y == Passwort:
        return "Succesfull login"
    else:
        return "Wrong Login"


server.register_function(test, "test")
print("Test!")
server.serve_forever()
