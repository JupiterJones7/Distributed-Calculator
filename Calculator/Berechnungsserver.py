import sys
from xmlrpc.server import SimpleXMLRPCServer


# Informationen
argumentList = sys.argv
hostAddress = '10.80.4.215'
port = '12345'
server = SimpleXMLRPCServer((hostAddress, int(port)))


# coordinator
def spooler(x, o, y):

    add = "+"
    sub = "-"
    mul = "*"
    div = "/"

    new_x = str(x)
    new_o = str(o)
    new_y = str(y)

    # addition
    if o == add:
        if calculator1(x, y) == calculator1a(x, y):
            r = calculator1(x, y)
            new_r = str(r)
            logger(new_x, new_o, new_y, "=", new_r)
            return calculator1(x, y)
        else:
            return "No result possible"

    # subtraction
    elif o == sub:
        if calculator2(x, y) == calculator2a(x, y):
            r = calculator2(x, y)
            new_r = str(r)
            logger(new_x, new_o, new_y, "=", new_r)
            return calculator2(x, y)
        else:
            return "No result possible"

    # multiplication
    elif o == mul:
        if calculator3(x, y) == calculator3a(x, y):
            r = calculator3(x, y)
            new_r = str(r)
            logger(new_x, new_o, new_y, "=", new_r)
            return calculator3(x, y)
        else:
            return "No result possible"

    # division
    elif o == div:
        if calculator4(x, y) == calculator4a(x, y):
            r = calculator4(x, y)
            new_r = str(r)
            logger(new_x, new_o, new_y, "=", new_r)
            return calculator4(x, y)
        else:
            return "No result possible"


# Calculators (+, -, *, /)
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


# Logs (file : log.txt)
def logger(a, b, c, d, e):

    with open('log.txt', 'w') as f:
        f.write(a + " " + b + " " + c + " " + d + " " + e)


# Server, Login -> Output
def network(u, p, x, o, y):

    username = "Timi"
    password = 12345

    if u == username and p == password:
        return "Successful login", spooler(x, o, y)
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
