
 def add(a,b):
     return a + b

def sub (a,b):
    return a - b

def mul (a,b):
    return a * b

def div(a,b):
    return a / b

def main():
    while True:
        print("simple calculator")
        print("options: ")
        print("1. Add")
        print("2. SUBtract")
        print("3. Multipy")
        print("4. Divide")
        print("5. Exit")

        choice =input("select an option (1-5)")


        if choice == "5":
            print("Exiting program good bye")
            break
        elif choice in {"1","2","3","4"}:
            try:
                num1 = float(input("Enter the first number:"))
                num2 = float(input("Enter the second number:"))

                if choice == "1":
                  result = add(num1, num2)
                  print(f"The Result of {num1} + {num2} is {result}")
                elif choice == "2":
                    result = sub(num1, num2)
                    print(f"The Result of {num1} - {num2} is {result}")
                elif choice == "3":
                    result = mul(num1, num2)
                    print(f"The Result of {num1} - {num2} is {result}")
                elif choice == "4":
                    result = div(num1, num2)
                    print(f"The Result of {num1} / {num2} is {result}")
        except ValueError:
                print("Invalid input. please enter numeric  vlaues. ")

main()