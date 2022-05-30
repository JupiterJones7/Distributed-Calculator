import xmlrpc.client
import sys


# Informationen
argumentsList = sys.argv
hostAddress = '127.0.0.1'
hostPort = '12345'
URI = "http://" + hostAddress + ":" + hostPort


# Eingaben
username = (input("Username: "))
password = int(input("Password: "))


# Verbindung zum Server
proxy = xmlrpc.client.ServerProxy(URI)


# Input Zahlen
num1 = float(input("Number 1: "))
operator = input("Operator: ")
num2 = float(input("Number 2: "))


# Ausgabe Login
print('{}'.format(proxy.network(username, password, num1, operator, num2)))
print(URI)
