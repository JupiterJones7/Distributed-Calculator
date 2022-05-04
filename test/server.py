import sys
import time
from datetime import datetime
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
        return "To Infinity and Beyond! Whee!"

def name():
    return hostAddress

def helpMe():
    return server.system_listMethods()

def serverTime():
    return time.strftime("%H:%M:%S")

def serverDatetime():
    return datetime.today().strftime('%Y-%m-%d')

server.register_function(name)
server.register_function(helpMe)
server.register_function(addition)
server.register_function(serverTime)
server.register_function(serverDatetime)
server.register_function(subtraction)
server.register_function(multiplication)
server.register_function(division)
server.serve_forever()
