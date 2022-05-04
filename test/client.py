import xmlrpc.client
import sys
import random

argumentsList = sys.argv
hostAddress = '10.80.4.132'
hostPort = '12345'

URI = "http://" + hostAddress + ":" + hostPort

num1 = int(random.randrange(10, 30))
num2 = int(random.randrange(10, 30))
proxy = xmlrpc.client.ServerProxy(URI)

print('{} + {} is {}'.format(num1, num2, proxy.addition(num1, num2)))
print('{} - {} is {}'.format(num1, num2, proxy.subtraction(num1, num2)))
print('{} * {} is {}'.format(num1, num2, proxy.multiplication(num1, num2)))
print('{} / {} is {}'.format(num1, num2, proxy.division(num1, num2)))
print(proxy.name())
print(proxy.helpMe())
print(proxy.serverTime())
print(proxy.serverDatetime())
