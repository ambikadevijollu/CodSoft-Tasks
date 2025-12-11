def banner():
    print("\n***********MINI CALCULATOR***********")
def get_number(label):
    while True:
        try:
            return float(input(f"Enter{label}:"))
        except ValueError:
            print("Please enter a valid value")
def calculator():
    while True:
        print("\nSelect Operation")
        print(" 1 = Addition")
        print(" 2 = Subtraction")
        print(" 3 = Multiplication")
        print(" 4 = Division")
        print(" 0 = Exit")
        option = input("Choose ").strip()
        if option == "00":
            print("Caculator closed")
            break
        if option not in {"1", "2", "3", "4"}:
            print("Invalid choice!")
            continue
        a = get_number("first number")
        b = get_number("second number")
        if option == "1":
            result = a + b
        elif option == "2":
            result = a - b 
        elif option == "3":
            result = a * b
        elif option == "4":
            if b == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = a / b 
        print(f"Result = {result}")
if __name__ == "__main__":
    calculator()