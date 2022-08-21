import os
import bcrypt
from dotenv import load_dotenv, set_key, find_dotenv
from cryptography.fernet import Fernet

with open(".env", "a") as file:
    pass

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

def hideFiles():
    os.system("attrib +h /s /d .env")
    os.system("attrib +h /s /d pm.db")

def hasHash():
    try:
        if os.environ["password_manager"] != "":
            return True
    except:
        return False
    
def hasKey():
    try:
        if os.environ["password_manager_key"] != "":
            return True
    except:
        return False

def checkUser():
    if not hasHash():
        print("Setup password")
        print("Do not forget this password or else you will not be able to recover your other passwords")
        password = input("Password: ")
        hashedPassword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        os.environ["password_manager"] = hashedPassword.decode()
        set_key(dotenv_file, "password_manager", os.environ["password_manager"])
        return True
    else:
        while True:
            password = input("Enter password: ")
            checkPassword = bcrypt.checkpw(password.encode(), os.environ["password_manager"].encode())
            if checkPassword:
                return True
        
       
def generateKey():
    if not hasKey():
        key = Fernet.generate_key()
        os.environ["password_manager_key"] = str(key, 'utf-8')
        set_key(dotenv_file, "password_manager_key", os.environ["password_manager_key"])
        
       
def encrypt(string):
    key = bytes(os.environ["password_manager_key"], "utf-8")
    fernet = Fernet(key)
    return fernet.encrypt(string.encode())
        
def decrypt(string):
    key = bytes(os.environ["password_manager_key"], "utf-8")
    fernet = Fernet(key)
    return fernet.decrypt(string).decode()