import sqlite3
from encryption import decrypt

def conn():
    try:
        connect = sqlite3.connect('pm.db')
    except Exception as e:
        print(e)
    return connect

def createDB():
    db = conn()
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Passwords (password PRIMARY KEY, service TEXT NOT NULL, email TEXT NOT NULL);")
    db.commit()
    
def store(password, service, email):
    exec_string = "INSERT INTO Passwords (password, service, email) VALUES(?, ?, ?)"
    db = conn()
    cursor = db.cursor()
    cursor.execute(exec_string, (password, service, email))
    db.commit()

def searchEmail(email):
    exec_string = "SELECT * FROM Passwords WHERE email = " + str(email)
    db = conn()
    cursor = db.cursor()
    cursor.execute(exec_string)
    results = cursor.fetchall()
    db.commit()
    if results:
        return results
    return None
    
def searchService(service):
    # decrypt db and compare with actual string
    exec_string = "SELECT * FROM Passwords"
    db = conn()
    cursor = db.cursor()
    cursor.execute(exec_string)
    results = cursor.fetchall()
    db.commit()
    if results:
        return results
    return None

def getAll():
    exec_string = "SELECT * FROM Passwords"
    db = conn()
    cursor = db.cursor()
    cursor.execute(exec_string)
    results = cursor.fetchall()
    db.commit()
    if results:
        return results
    return None

def getService(service):
    exec_string = "SELECT * FROM Passwords WHERE service = " + service
    db = conn()
    cursor = db.cursor()
    cursor.execute(exec_string)
    result = cursor.fetchone()
    db.commit()
    if result:
        return result
    return None