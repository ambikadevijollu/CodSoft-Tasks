import secrets
import string
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*_-+=?"
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password
def main():
    print("=====Password Generator====")
    try:
        length = int(input("Enter password length (min 6): "))
        if length < 6:
            print(" Length too short! Setting to minimum length 6.")
            length = 6
    except ValueError:
        print("Invalid input! Using default length 12.")
        length = 12
    password = generate_password(length)
    print("\nGenerated Password: ")
    print(password)
if __name__ == "__main__":
    main()
