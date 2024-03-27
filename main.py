import time as t

active = True
accountNum = 0
pin = 0

accounts = [0, 599.99, 10, 42, 64.32]

def mainmenu():
    print()
    print("Please enter a number for one of the following options: ")
    print("0 - Quick balance")
    print("1 - Log in / Account info")
    print("2 - Log out")
    print("3 - Forgot account number/PIN?")
    return input()

def quickprompt(acctNum, accts):
    print()
    while acctNum not in range(1, len(accts) - 1):
        acctNum = int(input("Please enter a valid account number to access a quick balance: "))
    print("Your balance is " + str(accounts[acctNum]) + ".")
    t.sleep(.5)
    return acctNum

def login():
    print()
    # Ask for account number
    # Ask for PIN
    # If valid, store both for this instance (simplifies things for UX)
    # Display account info (balance, transaction history, etc.)

def forgot():
    print()
    # Verify email
    # Ask recovery question(s) tied to the account
    # Print account number
    # If entered, store new password in database 

print("Hello, and welcome to the website for Northwest Bank! I'm your virtual assistant, Finch.")

while active:
    match(mainmenu()):
        case "0":
            accountNum = quickprompt(accountNum, accounts)
            continue
        case "1":
            login()
            continue
        case "2":
            accountNum = 0
            pin = 0
            continue
        case "3":
            forgot()
            continue



    t.sleep(.5)