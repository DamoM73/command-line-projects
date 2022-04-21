from tkinter import E


def main_menu():
    print("Do you wish to encrypt or decrypt or quit?")
    while True:
        response = input("Choose E D or Q > ").upper()
        if response in ("E","D","Q"):
            return response
    

def get_message():
    while True:
        message = input("Enter message > ").upper()
        if message.replace(" ","").isalpha():
            return message
        print("Only letters and spaces allowed.\n")


def get_key():
    while True:
        key = input("Enter key > ")
        if key.isdigit():
            key = int(key)
            return key % 26
        print("Please eneter a number.\n")
        
def shift_letters(message, key):
    new_message = ""
    for char in message:
        pos = SYMBOLS.index(char)
        new_message = new_message + SYMBOLS[(pos + key)%26]
    return new_message
        
    
# ----- MAIN PROGRAM ----- #

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Welcome to Caesar Cipher")
print("========================\n")
print("This program encodes and decodes letter from A-Z")
print("Spaces can be used to distinguish words.\n")

option = ""
while option != "Q":
    option = main_menu()
    
    # encoding
    if option == "E":
        message = get_message()
        key = get_key()
        print(shift_letters(message,key))
            