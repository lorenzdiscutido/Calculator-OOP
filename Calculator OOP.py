#Create a class named calculator
class Calculator:
#Add a function that ask the user to input two numbers
    def input(self):
        try:
            num1 = float(input("Please enter your first number:"))
            num2 = float(input("Please eneter your second number:"))
        except ValueError:
            print("Invalid. Please try again")
#Add a function that add the two numbers
    def add(self, num1, num2):
        try:
            sum = num1 + num2
            print("The sum of the two number is:", sum)
        except ValueError:
            print("Invalid. Please try again")  

#Add a function that subtract the two numbers
    def subtract(self, num1, num2):
        try:
            difference = num1 -num2
            print("The difference of the two number is:", difference)
        except ValueError:
            print("Invalid. Please try again")

#Add a function that multiply the two numbers
    def multiply(self, num1, num2):
        try:
            product = num1*num2
            print("The product of the two number is:", product)
        except ValueError:
            print("Invalid. Please try again")
#Add a function that divide the two numbers
    def divide(self, num1, num2):
        try:
            quotient = num1/num2
            print("The quotient of the two number is", quotient)
        except (ValueError, ZeroDivisionError):
            print("Invalid. Please try again")