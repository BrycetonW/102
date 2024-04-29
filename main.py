import time as t
import unittest as ut
import mysql.connector

accounts = []
accountID = -1
password = ""

class TestIsString(ut.TestCase): # I really wasn't sure how to implement unit testing in a way that would be relevant for this project
    def test_string(self): # Based on the one Canvas page about unit testing, it seems to be akin to printing out a value or the program catching an error
        self.assertTrue(isinstance(password, str)) # I used booleans and while loops in my program for a similar effect, but I have an example of unit testing here

def mainmenu(acctID, accts):
    print("Please enter a number for one of the following options: ")
    if acctID in range(1, len(accts)):
        print("1 - Check balance")
        print("2 - Make transaction")
        print("3 - Log out")
        print("4 - Close account")
    else:
        print("0 - Exit")
        print("1 - Quick balance")
        print("2 - Log in")
        print("3 - Sign up")
    return input()

def quickprompt(acctID, accts):
    while acctID not in range(1, len(accts)):
        acctID = int(input("Please enter a valid account ID to access a quick balance: "))
    print("Your balance is " + str(accounts[acctID - 1][2]) + ".")
    t.sleep(.5)

def signup():
    connection = mysql.connector.connect(user = "root", database = "acct_info", password = "BrycetonW_E102")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO acct_info.acct_table (Password, Balance) VALUES ('{input("Enter a password for your account: ")}', 0)")
    print(f"Your account ID is {cursor.lastrowid}. Keep it somewhere safe, you'll need it to sign in!")
    connection.commit()
    cursor.close()
    connection.close()
    t.sleep(1)

def login(acctID, key, accts):
    while acctID not in range(1, len(accts)): # Ask for account ID
        acctID = int(input("Please enter your account ID to log in: "))
    while str(key) != str(accounts[acctID - 1][1]): # Ask for password
        key = input("Password: ")
    # If valid, store both for this instance (simplifies things for UX)
    global accountID
    accountID = acctID # Storing account ID for current session
    global password
    password = key # Storing password for current session
    print("Would you like to change your password? [y/n]")
    if input().lower == "y":
        connection = mysql.connector.connect(user = "root", database = "acct_info", password = "BrycetonW_E102")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO acct_info.acct_table (ID, Password, Balance) VALUES ({acctID}, '{input("Enter a password for your account: ")}', 0)")
        print(f"Your password has been changed. Keep it somewhere safe, you'll need it to sign in!")
        connection.commit()
        cursor.close()
        connection.close()
        t.sleep(1)
    # Display account info (ID, password, balance, etc.)
    
def transaction(acctID, key, accts):
    print("Would you like to deposit or withdraw?")
    ans = input()
    while ans.lower() != "deposit" and ans.lower() != "withdraw":
        ans = input()
    if ans.lower != "deposit":
        connection = mysql.connector.connect(user = "root", database = "acct_info", password = "BrycetonW_E102")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO acct_info.acct_table (ID, Password, Balance) VALUES ({acctID}, '{key}', {accts[acctID - 1][2] + int(input("How much would you like to deposit? "))})")
        connection.commit()
        cursor.close()
        connection.close()
        
    else:
        connection = mysql.connector.connect(user = "root", database = "acct_info", password = "BrycetonW_E102")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO acct_info.acct_table (ID, Password, Balance) VALUES ({acctID}, '{key}', {accts[acctID - 1][2] - int(input("How much would you like to withdraw? "))})")
        connection.commit()
        cursor.close()
        connection.close()


def close(acctID):
    print("Are you sure you want to close your account? [y/n]")
    if input().lower != "y": # We're ignoring any other input just in case
        connection = mysql.connector.connect(user = "root", database = "acct_info", password = "BrycetonW_E102")
        cursor = connection.cursor(buffered=True)
        testQuery = (f"DELETE FROM acct_table WHERE ID={acctID}")
        cursor.execute(testQuery)
        cursor.close()
        connection.close()
    else:
        print("Input was not 'y'. Account closure cancelled.")
        t.sleep(.5)
        

while True:
    connection = mysql.connector.connect(user = "root", database = "acct_info", password = "BrycetonW_E102")
    cursor = connection.cursor(buffered=True)
    testQuery = ("SELECT * FROM acct_table")
    cursor.execute(testQuery)
    accounts = []
    for i in cursor:
        accounts.append(i)
    cursor.close()
    connection.close()

    if accountID in range(1, len(accounts)) and password != accounts[accountID][1]:
        match(mainmenu(accountID, accounts)):
            case "1":
                quickprompt(accountID, accounts)
                continue
            case "2":
                transaction(accountID, password, accounts)
                continue
            case "3":
                accountID = -1
                username = ""
                password = ""
                break
            case "4":
                close(accountID)
                continue
    else:
        match(mainmenu(accountID, accounts)):
            case "0":
                accountID = -1
                username = ""
                password = ""
                break
            case "1":
                quickprompt(accountID, accounts)
                continue
            case "2":
                login(accountID, password, accounts)
                continue
            case "3":
                signup()
                continue
    t.sleep(.5)

# connection.close()