# ******************************
# GELOS ENTERPISES USER LOGIN
# AUTHOR: HARRY MCLEAN
# EMAIL: Hazmclean92@gmail.com | harry.mclean4@studytafensw.edu.au
# CREATED 29-10-2022
# LAST UPDATE: 29-10-2022
# *****************************

# imported libraries

from datetime import datetime
import csv
import time
import random
import string
from xml.sax.xmlreader import AttributesImpl

from mysqlx import AddStatement

# GLOBAL VARIABLES

lCase = 'abcdefghijklmnopqrstuvwxyz'
uCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '123456789'
alNum = '~!@#$%^&*()_+'
allChar = lCase + uCase + nums + alNum


# USER DEFINED FUNCTIONS
def convertdt():
    todaysdt = datetime.today()
    # CONVERT TO 12 HOUR FORMAT
    todaysdtformatted = todaysdt.strftime('%Y/%m/%d %I:%M:%S')
    print(todaysdtformatted)


def loginMsg():
    print("Next Login Message")


# def passwordGenerator(length):

    # def passwordValid():


def options():
    match UserOption:
        case "1":
            attempts = 0
            while attempts < 3:
                userName = input("Please Enter Username: ")
                passW = input("Please Enter Password: ")

                for line in open('accounts.txt', 'r').readlines():
                    userLogin = line.split(', ')
                    print(userLogin[0], userLogin[1])
                    if (userName == userLogin[0] and passW == userLogin[1]):

                        print('Login Successful')
                        attempts = 3
                        break

                    else:
                        if (attempts < 3):
                            print("Credentials Incorrect")
                            attempts += 1
                            print(attempts)
                            break
                        elif (attempts > 3):
                            choice = input(
                                "Three incorrect attempts have been made would you like to reset password Y or N? ")
                            if (choice == 'y'):
                                print('reset')
                                quit()
                            elif (choice == 'n'):
                                print('quit')
                                exit()

        case "2":
            while True:
                # Validate USERNAME
                print(
                    "Please Enter a Username that is between 6 & 15 characters long with 1 uppercase character")
                newUsr = input("Username: ")

                if (len(newUsr) < 6 or len(newUsr) > 15):
                    print("UserName must be between 6 and 15 character in length")

                while True:
                    for line in open('accounts.txt', 'r').readlines():
                        userLogin = line.split(', ')
                        if userLogin[0] == newUsr:
                            print("Username is taken")
                            break
                        else:
                            for i in newUsr:
                                if (i.isupper()):
                                    while True:
                                        choice = input(
                                            "Would you like to generate a password Y or N? ")
                                        if (choice == 'y'):
                                            # GENERATE PASSWORD WITH 8 CHARACTERS
                                            lCase = string.ascii_lowercase
                                            uCase = string.ascii_uppercase
                                            num = string.digits
                                            alNum = string.punctuation

                                            all = lCase + uCase + num + alNum
                                            temp = random.sample(all, 8)
                                            newPass = "".join(temp)
                                            break
                                        elif (choice == 'n'):
                                            print(
                                                "Please enter a password that meets GELOS standards\n")
                                            newPass = input("Password: ")
                                            if (len(newPass) >= 8):
                                                for char in newPass:
                                                    if (char.isdigit() == True):
                                                        break

                                                for char in newPass:
                                                    if (char.isupper() == True):
                                                        break

                                                for char in newPass:
                                                    if (char.islower() == True):
                                                        break

                                                for char in newPass:
                                                    if (char.isalnum() == True):
                                                        break
                                                break
                                            else:
                                                print(
                                                    "Password does not meet GELOS Standards")
                                            # break

                            while True:            # VALIDATE EMAIL
                                print(
                                    "Please enter a valid email\n")
                                newEmail = input("Email: ")
                                print(newEmail)
                                # for i in newEmail:
                                if ('@' in newEmail):

                                    # WRITE TO FILE
                                    print(
                                        "User account registered\nprogram will now close")
                                    print(newUsr, newPass, newEmail)
                                    f = open('accounts.txt', 'a+')
                                    f.write('\n' + str(newUsr) + ', ' +
                                            str(newPass) + ', ' + str(newEmail))
                                    f.close
                                    time.sleep(2)
                                    exit()

                                    # break
                                else:
                                    print('Not a valid Email Address')
                                # BREAK OUT OF PROGRAM
                        # break
        case "3":
            print("Reset Password Selected")
        case "4":
            print("View Accounts Selected")
        case "5":
            time.sleep(2)
            exit()


# PROGRAM
print("******************************\n  GELOS ENTERPISES USER LOGIN\n******************************")
convertdt()
loginMsg()
print("Please press the corressponding key for the option you would like")
print(" 1 - LOGIN\n 2 - REGISTER\n 3 - RESET PASSWORD\n 4 - VIEW ACCOUNTS\n 5 - EXIT")
UserOption = input(": ")
options()
