################################################################################
# Generate a password of decent, user configurable complexity
################################################################################

# Third Party Imports
import sys
import random
import requests
import json
import random
import pyperclip # Gonna need to install this one if its not already added

# Configuration Options
url = "https://github.com/dwyl/english-words/raw/master/words_dictionary.json"
passwordType = 'basic'
humanPasswordMaxLength = 16
complexPasswordLength = 32

# Global Variables
print("Generating dictionary cache from ", url, "...")
dictionary = requests.get(url).json()
dictionary_list = []
for i in dictionary:
    dictionary_list.append(i)
isRunning = True


# Evaluate the given password to make sure it complies with default Windows
#   password requirements. (lower case, upper case, number, special character,
#   and at least 8 characters in lengths)
def evaluateCompliance(password, maxLength):
    lower = False
    upper = False
    symbol = False
    digit = False
    if len(password) > 8:
        for i in range(0, len(password)):
            if ord(password[i]) >= 97 and ord(password[i]) <= 122:
                lower = True
            elif ord(password[i]) >= 65 and ord(password[i]) <= 90:
                upper = True
            elif ord(password[i]) >= 33 and ord(password[i]) <= 47:
                symbol = True
            elif ord(password[i]) >= 48 and ord(password[i]) <= 57:
                digit = True

            if lower and upper and digit and symbol:
                return True

    # True means password met requirements while False means it did not
    return False


# Generate a password designed for every day human use
#   MUST comply with default windows password requirements at least
def generateHumanPassword(maxLength=16):
    global dictionary
    password = ''
    isRunning = True
    symbolControl = 0
    digitControl = 0
    lowerControl = 0
    upperControl = 0
    while(isRunning):
        nextAddition = random.randint(0, 4)

        if nextAddition == 0 and lowerControl < 3:
            password += dictionary_list[random.randint(0, len(dictionary_list))]
            lowerControl +=1

        elif nextAddition == 1 and upperControl < 3:
            password += dictionary_list[random.randint(0, len(dictionary_list))].upper()
            upperControl +=1

        elif nextAddition == 2 and symbolControl < 4:
            password += str(chr(random.randint(33, 64)))
            symbolControl += 1

        elif nextAddition == 3 and digitControl < 4:
            password += str(chr(random.randint(48, 57)))
            digitControl += 1

        elif nextAddition > 4:
            print("Attempted unavailable option for password creation")

        if lowerControl == 3:
            lowerControl +=1

        if upperControl == 3:
            upperControl +=1

        if digitControl == 4:
            digitControl += 1

        if symbolControl == 4:
            symbolControl += 1

        # restart the process...
        if len(password) > maxLength:
            password = ''
            isRunning = True
            symbolControl = 0
            digitControl = 0
            lowerControl = 0
            upperControl = 0

        isRunning = not evaluateCompliance(password, maxLength)

    return password


# Generate a password designed for system or paranoid security guy use
def generateComplexPassword(charCount=16):
    password = ''
    print("Generating Complex password of ", charCount, " characters")
    for i in range(0, charCount):
        password += str(chr(random.randint(33, 126)))

    return password


# Prompt user for yes or no. yes returns True, no returns False
def simplePrompt(prompt):
    while(True):
        response = input(prompt)
        if response == "Y" or response == "y" or response == "yes" or response == "YES" or response == "Yes":
            return True
        elif response == "N" or response == "n" or response == "no" or response == "NO" or response == "No":
            return False
        else:
            print("Invalid option entered, please answer yes or no.\n")


################################################################################
# MAIN
################################################################################
def main():
    global passwordType
    global humanPasswordMaxLength
    global complexPasswordLength
    global passwordType

    isRunning = True

    myPassword = ''

    while(isRunning):
        myPassword = ''
        if passwordType == 'basic':
            print("generating basic password")
            myPassword = generateHumanPassword(humanPasswordMaxLength)
        elif passwordType == 'complex':
            myPassword = generateComplexPassword(complexPasswordLength)

        print("\nPassword: \t", myPassword, "\n")
        try:
            pyperclip.copy(myPassword)
            print("Password has been copied to your clipboard\n")
        except:
            print("I am unable to copy the password to your clipboard for you.")

        isRunning = simplePrompt("Would you like me to generate another password? (Y/N)")


if __name__ == "__main__":
    main()
