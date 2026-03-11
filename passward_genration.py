import random
import string
import pyperclip

print("====== Password Genration =======")

times = int(input("Enter how many password you want to gerate = "))

length = int(input("Enter the length of password = "))

charaters =  string.ascii_letters + string.digits + string.punctuation

for i in range(times):
    
    password = ""

    for j in range(length):

        password += random.choice(charaters)

    print("Password Genration =", password)

    pyperclip.copy(password)
    print("Password copyed to clipboard!\n")