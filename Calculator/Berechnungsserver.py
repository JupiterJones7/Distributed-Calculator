import sys
from xmlrpc.server import SimpleXMLRPCServer

argumentList = sys.argv
hostAddress = '10.80.4.215'
port = '12345'
server = SimpleXMLRPCServer((hostAddress, int(port)))


def addition(x, y):
    return x + y


def calculator2(x, y):
    return x + y, x * y


def calculator3(x, y):
    return x - y, x / y


def calculator4(x, y):
    return x - y, x * y


def calculator5(x, y):
    return x + y, x / y


def test(x, y, d, c):

    username = "Timi"
    password = 12345

    if x == username and y == password:
        return "Successful login", addition(d, c)
    else:
        return "Wrong Login"


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "You cannot divide 0"


server.register_function(test, "test")
server.register_function(addition)
server.register_function(subtraction)
server.register_function(multiplication)
server.register_function(division)
server.serve_forever()
