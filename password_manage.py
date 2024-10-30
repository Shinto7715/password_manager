import hashlib
import getpass

password_manager = {}

def create_account():
  username = input("Enter your prefered username: ")
  password = getpass.getpass("Enter your password: ")
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  password_manager[username] = hashed_password
  print("Account successfully created")

def login():
  username = input("Enter your username: ")
  password = getpass.getpass("Enter your password: ")
  hashed_password = hashlib.sha256(password.encode()).hexdigest()

  if username in password_manager.keys() and hashed_password == password_manager[username]:
    print("Login Successful!")

  else:
    print("Error: Either your username or password is incorrect.")

def main():
  while True:
    choice = input("Please select if you want to login (1), create an account (2), or exit (0): ")

    match choice:

      case '1':
        login()

      case '2':
        create_account()

      case '0':
        break

      case _:
        print("Invalid input")

if __name__ == '__main__':
  main()