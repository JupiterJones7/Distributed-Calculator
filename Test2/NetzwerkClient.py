import xmlrpc.client
import sys

argumentsList = sys.argv
hostAddress = '127.0.0.1'
hostPort = '12345'

URI = "http://" + hostAddress + ":" + hostPort

num1 = (input("Zahl 1: "))
num2 = int(input("Zahl 2: "))
proxy = xmlrpc.client.ServerProxy(URI)


print('{}'.format(proxy.test(num1, num2)))


