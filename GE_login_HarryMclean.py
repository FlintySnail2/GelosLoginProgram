# ******************************
# GELOS ENTERPISES USER LOGIN
# AUTHOR: HARRY MCLEAN
# EMAIL: Hazmclean92@gmail.com | harry.mclean4@studytafensw.edu.au
# CREATED 29-10-2022
# LAST UPDATE: 29-10-2022
# *****************************

# imported libraries

from datetime import datetime, date
import time
import csv
import random
import string

# GLOBAL VARIABLES

lCase = 'abcdefghijklmnopqrstuvwxyz'
uCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '123456789'
alNum = '~!@#$%^&*()_+'
allChar = lCase + uCase + nums + alNum


# def programStart():


# USER DEFINED FUNCTIONS


def convertdt():
    todaysdt = datetime.today()
    # CONVERT TO 12 HOUR FORMAT
    todaysdtformatted = todaysdt.strftime('%d/%m/%Y %I:%M:%S')
    print(todaysdtformatted)

# def generatePassword(newPass):
#     newPass = ''
#     lCase = string.ascii_lowercase
#     uCase = string.ascii_uppercase
#     num = string.digits
#     alNum = string.punctuation

#     all = lCase + uCase + num + alNum
#     temp = random.sample(all, 8)
#     newPass = "".join(temp)


def resetPassword():
    choice = input('Would you like to reset your password? Y or N: ')
    if (choice.lower() == "y"):
        newPass = input("Would you like to generate a new password? Y or N: ")
        if (newPass.lower() == 'y'):
            lCase = string.ascii_lowercase
            uCase = string.ascii_uppercase
            num = string.digits
            alNum = string.punctuation

            all = lCase + uCase + num + alNum
            temp = random.sample(all, 8)
            newPass = "".join(temp)

            f = open('accounts.txt', 'a+')
            f.write

    elif (choice.lower() == 'n'):
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
        else:
            print(
                "Password does not meet GELOS Standards")


# def passwordGenerator(length):

    # def passwordValid():


def options():
    match UserOption:
        case "1":
            while True:
                attempts = 0
                if (attempts < 3):
                    while True:
                        userName = input("Please Enter Username: ")
                        passW = input("Please Enter Password: ")

                        for line in open('accounts.txt', 'r').readlines():
                            userLogin = line.split(', ')
                            if (userName == userLogin[0] and passW == userLogin[1]):
                                if (userLogin[4] - datetime.now() < 100):
                                    print('Login Successful')
                                    attempts = 3
                                    break

                                elif (userLogin[4] - datetime.now() >= 100 and userLogin[4] - datetime.now() < 120):
                                    print(
                                        f'You have { userLogin[4] - datetime.now()}')

                            else:
                                if (attempts < 3):
                                    print("Credentials Incorrect")
                                    attempts += 1
                                    print(attempts)
                                    break

                                elif (attempts > 3):

                                    break
                                break
                else:
                    choice = input(
                        "Three incorrect attempts have been made would you like to reset password Y or N? ")
                    if (choice == 'y'):
                        resetPassword()
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
                            # INFINITE LOOP
                            break
                        else:
                            for i in newUsr:
                                if (i.isupper()):
                                    while True:
                                        choice = input(
                                            "Would you like to generate a password Y or N? ")
                                        if (choice.lower() == 'y'):
                                            # GENERATE PASSWORD WITH 8 CHARACTERS
                                            lCase = string.ascii_lowercase
                                            uCase = string.ascii_uppercase
                                            num = string.digits
                                            alNum = string.punctuation

                                            all = lCase + uCase + num + alNum
                                            temp = random.sample(all, 8)
                                            newPass = "".join(temp)
                                            break
                                        elif (choice.lower() == 'n'):
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
                                staticDt = datetime.today()
                                passwCreate = staticDt.strftime('%Y/%m/%d')
                                lastLogin = staticDt.strftime('%Y/%m/%d')
                                loginMsg = ' '

                                print(newEmail)
                                # for i in newEmail:
                                if ('@' in newEmail):

                                    # WRITE TO FILE
                                    print(
                                        "User account registered\nprogram will now close")
                                    print(newUsr, newPass, newEmail)
                                    f = open('accounts.txt', 'a+')
                                    f.write('\n' + str(newUsr) + ', ' +
                                            str(newPass) + ', ' + str(newEmail) + ', ' + str(loginMsg) + ', ' + str(lastLogin) + ', ' + str(passwCreate))
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
            resetPassword()

        case "4":
            # while True:
            header = "Username    Password     Email      Next Login message        Last Login       Password Reset"
            print('Please enter Administrator credentials\n')
            # sysUsr = input('Enter Username: ')
            # sysPass = input('Enter Password: ')
            # if (sysUsr == 'SAadmin' and sysPass == 'adminSA'):
            print(header)
            with open('accounts.txt', 'r') as f:
                accounts = f.read()
                print(accounts)
                f.close()
            # else:
            #     tryagain = input("Invalid credential Try again? Y or N: ")
            #     if (tryagain.lower == 'y'):
            #         return True

            #     elif (tryagain.lower == 'n'):
            #         return False
            #     break

        case "5":
            end_time = datetime.now()
            end = end_time.strftime("%M:%S")
            t2 = datetime.strptime(end, "%M:%S")
            timeInUse = t2 - t1
            print(
                f'You have use the system of a duration of {timeInUse}')
            time.sleep(2)
            exit()


# PROGRAM
try:
    while True:
        start_time = datetime.now()
        start = start_time.strftime("%M:%S")
        t1 = datetime.strptime(start, "%M:%S")
        print("******************************\n  GELOS ENTERPISES USER LOGIN\n******************************")
        convertdt()

        # print(start.strftime("%M:%S"))

        # loginMsg()
        print("Please press the corressponding key for the option you would like")
        print(
            " 1 - LOGIN\n 2 - REGISTER\n 3 - RESET PASSWORD\n 4 - VIEW ACCOUNTS\n 5 - EXIT")
        UserOption = input(": ")
        options()
except KeyboardInterrupt:
    print("Killed Program")
