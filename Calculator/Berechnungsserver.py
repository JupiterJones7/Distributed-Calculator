import sys
from xmlrpc.server import SimpleXMLRPCServer

argumentList = sys.argv
hostAddress = '10.80.4.215'
port = '12345'
server = SimpleXMLRPCServer((hostAddress, int(port)))


def spooler(x, o, y):

    add = "+"
    sub = "-"
    mul = "*"
    div = "/"

    if o == add:
        if calculator1(x, y) == calculator1a(x, y):
            return calculator1(x, y)
        else:
            return "No result possible"

    elif o == sub:
        if calculator2(x, y) == calculator2a(x, y):
            return calculator2(x, y)
        else:
            return "No result possible"

    elif o == mul:
        if calculator3(x, y) == calculator3a(x, y):
            return calculator3(x, y)
        else:
            return "No result possible"

    elif o == div:
        if calculator4(x, y) == calculator4a(x, y):
            return calculator4(x, y)
        else:
            return "No result possible"


def calculator1(x, y):
    return x + y


def calculator1a(x, y):
    return x + y


def calculator2(x, y):
    return x - y


def calculator2a(x, y):
    return x - y


def calculator3(x, y):
    return x * y


def calculator3a(x, y):
    return x * y


def calculator4(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "You cannot divide 0"


def calculator4a(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "You cannot divide 0"


def network(x, y, d, o, c):

    username = "Timi"
    password = 12345

    if x == username and y == password:
        return "Successful login", spooler(d, o, c)
    else:
        return "Wrong Login"


server.register_function(spooler)
server.register_function(calculator1)
server.register_function(calculator1a)
server.register_function(calculator2)
server.register_function(calculator2a)
server.register_function(calculator3)
server.register_function(calculator3a)
server.register_function(calculator4)
server.register_function(calculator4a)
server.register_function(network)
server.serve_forever()
