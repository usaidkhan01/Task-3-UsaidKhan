import secrets
import string


def generate_password(length, use_special=False):
    characters = string.ascii_letters + string.digits

    if use_special:
        characters += string.punctuation

    password = "".join(secrets.choice(characters) for _ in range(length))

    return password


while True:
    print("\n===== Random Password Generator =====")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password length should be at least 4.")
                continue

            special = input("Include special characters? (y/n): ").lower()

            if special == "y":
                password = generate_password(length, True)
            else:
                password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        print("Thank you for using Password Generator!")
        break

    else:
        print("Invalid choice.")