def main_menu():
    print("Do you wish to encrypt or decrypt or quit?")
    while True:
        response = input("Choose E D or Q > ").upper()
        if response in ("E","D","Q"):
            return response
    

def get_message():
    while True:
        message = input("Enter message > ")
    
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
        