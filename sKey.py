
import hashlib
import os


def init_keys():
    name = input("Enter your name:\n")
    if os.path.exists(name):
        print('User already exists.')
    else:
        user_keys = input('Enter your secret password to generate S/Key:\n')
        try:
            keys = open(name + "Keys.txt", "w")
            # num = int(input('Enter a number of password you want to create \n'))
            for i in range(1024):
                user_keys = hashlib.sha3_256(user_keys.encode('utf-8')).hexdigest()
                keys.write(user_keys+'\n')
            key = hashlib.sha3_256(user_keys.encode('utf-8')).hexdigest()
            f = open(name, "w")
            print("Your keys are created")
            f.write(key)
            keys.close()
            f.close()
        except Exception as e:
            print(e)


def login():
    name = input("Enter a user name:\n")
    try:
        f = open(name, "r")
        key = f.read()
        password = input("Enter password:\n")
        hash_password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
        if hash_password == key:
            print("Login successful!")
            f = open(name, "w")
            f.write(password)
            f.close()
        else:
            print("Invalid password!")
    except FileNotFoundError:
        print("User does not exist.")


def main():
    while True:
        try:
            option = int(input('\nChoose Option:\n1. Register\n2. Login\n3. Quit\n'))
            if option == 1:
                init_keys()
            elif option == 2:
                login()
            elif option == 3:
                exit(0)
        except ValueError:
            print('Invalid input. Please enter a number')


if __name__ == "__main__":
    main()