from db import store, getAll as getAllDB
from encryption import encrypt, decrypt
import pyperclip


def set():
    service = input("Service Name: ")
    email = input("Email: ")
    password = input("Password: ")
    service = encrypt(service)
    email = encrypt(email)
    password = encrypt(password)
    store(password, service, email)
    print("inserted!")
    
def searchEmail():
    email = input("Email: ")
    results = getAllDB()
    if results != None:
        for result in results:
            if decrypt(result[2]) == email:
                printResult(result)
                return
    print("none found")
    
def searchService():
    service = input("Service Name: ")
    results = getAllDB()
    if results != None:
        for result in results:
            if decrypt(result[1]) == service:
                printResult(result)
                return
    print("none found")
    
def printAll():
    results = getAllDB()
    if results != None:
        for result in results:
            printResult(result)
    print("you have none")

def getServicePassword():
    service = input("Service Name: ")
    results = getAllDB()
    if results != None:
        for result in results:
            if decrypt(result[1]) == service:
                pyperclip.copy(decrypt(result[0]))
                print("copied!")
                return
    print("none found")
    
    
    
def printResult(result):
    print("-"*20)
    print("Service: " + decrypt(result[1]))
    print("Email: " + decrypt(result[2]))
    