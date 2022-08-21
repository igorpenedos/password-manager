from encryption import checkUser, hideFiles
import sys
from db import createDB
from encryption import generateKey
from commands import set, searchEmail, searchService, printAll, getServicePassword

if checkUser():
    generateKey()
    createDB()
    hideFiles()
    print("""
          Commands:
          1. set 
          2. get by service
          3. get by email
          4. print all services
          5. get password by service name
          q. quit
          """)
    while True:
        command = input("command: ")
        if command == "1":
            set()
        elif command == "2":
            searchService()
        elif command == "3":
            searchEmail()
        elif command == "4":
            printAll()
        elif command == "5":
            getServicePassword()
        elif command == 'q':
            sys.exit("Exiting.....")
        else:
            print("Incorrect input")
        print("-"*20)