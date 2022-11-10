#!/usr/bin/env python


import random, string

number_of_digits = int(input("How many digits should be included:" ))
number_of_punctuation_characters = int(input("How many characters should be included:" ))
characters = string.ascii_letters + string.digits + string.punctuation

number_of_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("Provide the password length: "))

def randomize_password(password):
    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)

for password_index in range(number_of_passwords):
    password = ""

    for digits_index in range(number_of_digits):
        password = password + random.choice(string.digits)

    for punctuation_index in range(number_of_punctuation_characters):
        password = password + random.choice(string.punctuation)

    for index in range(password_length - number_of_digits - number_of_punctuation_characters):
        password = password + random.choice(string.ascii_letters)

    print("Password {} generated: {}".format(password_index, randomize_password(password)))