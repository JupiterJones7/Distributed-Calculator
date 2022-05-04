import xmlrpc.client
import sys

argumentsList = sys.argv
hostAddress = '10.80.4.233'
hostPort = '12345'

URI = "http://" + hostAddress + ":" + hostPort

num1 = int(input("Zahl 1: "))
num2 = int(input("Zahl 2: "))
proxy = xmlrpc.client.ServerProxy(URI)

print('{} + {} is {}'.format(num1, num2, proxy.addition(num1, num2)))
print('{} - {} is {}'.format(num1, num2, proxy.subtraction(num1, num2)))
print('{} * {} is {}'.format(num1, num2, proxy.multiplication(num1, num2)))
print('{} / {} is {}'.format(num1, num2, proxy.division(num1, num2)))
print(URI)
