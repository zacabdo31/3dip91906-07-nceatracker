#this program is a calculator using classes

class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y #Constructor

    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        if self.y == 0:
            return 'Error: Division by zero' #These are the methods
        

#Asking Inputs

x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

calc = Calculator(x,y) #instantiation
print(f'Addition: {calc.add()}')
print(f'Subtraction: {calc.sub()}')
print(f'Multiplication: {calc.mul()}')
print(f'Division: {calc.div()}') #Assigning methods to objects
    
