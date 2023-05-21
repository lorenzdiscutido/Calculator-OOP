#import the class from other
from Calculator_OOP import Calculator

#use variables for easy typing
calc = Calculator()

#show the user the options
calc.option()

while True:
    #ask the user for their numbers
    num1 = calc.input()
    num2 = calc.input()

    #ask the user what operation they like to use
    option = calc.operation()
    if option == "1":
        sum = calc.add(num1, num2)
    elif option == "2":
        difference = calc.subtract(num1, num2)
    elif option == "3":
        product = calc.multiply(num1, num2)