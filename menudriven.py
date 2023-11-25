num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

while True:
    print("Choose the option from below: ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")


    option = eval(input("Enter the option from above menu: "))

    if option == 1:
        Sum = num1 + num2 
        print("Sum of two numbers is",Sum)
        input()

    elif option == 2:
        Diff = num1 - num2
        print("Difference of two numbers is",Diff) 
        input()
    
    elif option == 3:
        product = num1 * num2       
        print("The product of two numbers is",product)
        input()
    
    elif option == 4 :
        Div = num1/num2
        print("The quotient of two numbers is",Div)    
        input()

    else:
        print("Enter the correct option")
