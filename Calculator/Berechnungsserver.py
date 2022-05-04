import sys
from xmlrpc.server import SimpleXMLRPCServer

argumentList = sys.argv
hostAddress = '10.80.4.233'
port = '12345'
server = SimpleXMLRPCServer((hostAddress, int(port)))

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "You cannot divide 0"



server.register_function(addition)
server.register_function(subtraction)
server.register_function(multiplication)
server.register_function(division)
