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