import string

""" The user inputs the chosen password. """
password = input("Enter your password: ")


""" Checks if there are any upper, lower, special characters and numbers """
lowercase = any([1 if i in string.ascii_lowercase else 0 for i in password])
uppercase = any([1 if i in string.ascii_uppercase else 0 for i in password])
special_characters = any([1 if i in string.punctuation else 0 for i in password])
numbers = any([1 if i in string.digits else 0 for i in password])

list_to_check = [lowercase, uppercase, special_characters, numbers]

amount = 0
length = len(password)

""" Checking if the password is in a file containing top 1000 passwords
to prevent dictionary attacks """

with open('common_passwords.txt', 'r') as pfile:
    common_passwords = pfile.read().splitlines()

if password in common_passwords:
    print("Your password is among the top 1000 most used passwords. Password Strength: 0 / 7")
    exit()

    
if length > 8:
    amount += 1
if length > 13:
    amount += 1
if length > 18:
    amount += 1
if length > 23:
    amount += 1

print("The length of the password is:", length, ". You have received", amount, "point(s) for strength.")

if sum(list_to_check) > 1:
    amount += 1
if sum(list_to_check) > 2:
    amount += 1
if sum(list_to_check) > 3:
    amount += 1

print("The password has ", sum(list_to_check),"distinctive type(s) of characters. You have received ", sum(list_to_check) - 1," point(s) for strength.")

if amount < 4:
    print("The password is NOT strong. Your password strength is: ", amount, " / 7")
if amount == 4:
    print("The password is acceptable. However, it could be better. Your password strength is: ", amount," / 7")
if amount >4 and amount <6:
    print("The password is good. Your password strength is: ", amount," / 7")
if amount > 6:
    print("The password is strong. Your password strength is:", amount, " / 7")




