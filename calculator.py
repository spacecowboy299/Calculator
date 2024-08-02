#defining functions
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return 'Undefined'
    else:
        return x / y
    
#starts and defines the calculator function loop
def calculator():
    while True:
                #operator options
                Option1 = "1. Addition"
                Option2 = "2. Subtraction"
                Option3 = "3. Multiplication"
                Option4 = "4. Division"

                print(Option1)
                print(Option2)
                print(Option3)
                print(Option4)

                print("Select an option 1-4")

                choice = input()

                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))

                #conditons to check and execute calculations
                if choice == '1':
                 print(add(num1, num2))
                elif choice == '2':
                    print(sub(num1, num2))
                elif choice == '3':
                    print(mult(num1, num2))
                elif choice == '4':
                   print(div(num1, num2))
                else:
                    print("Select a valid option")
#recalls the caluculator to keep the loop
calculator()                   