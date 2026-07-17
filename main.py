from notes import run_notes
from weather import get_weather
from passwordGenerator import generate_password
from tasks import run_tasks

def notes():
    run_notes()

def weather():
    get_weather()


def password_generator():
    while True:
        try:
            length = int(input("Enter the desired password length (8-30): "))
            if length < 8 or length > 30:
                raise ValueError("Password length must be between 8 and 30.")
        except ValueError as e:
            print(e)
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
            break

def tasks():
    run_tasks()

def app():
    while True:
        try:
            print("1. Notes\n2. Weather\n3. Password Generator\n4. Tasks\n5. Exit")
            choice = int(input("Enter your choice: "))
            if choice not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid choice.")
        except ValueError:
            print("Invalid Choice!")
        else:
            if choice == 1:
                notes()
            elif choice == 2:
                weather()
            elif choice == 3:
                password_generator()
            elif choice == 4:
                tasks()
            else:
                break


app()