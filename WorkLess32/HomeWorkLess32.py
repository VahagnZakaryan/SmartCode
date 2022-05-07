
class Calculator:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    def sum (self):
        return print(x1 + x2)
    def differ (self):
        return  print(x1 - x2)
    def mult (self):
        return print(x1 * x2)
    def divide(self):
        return print(x1 / x2)

print('1)Sum')
print('2)Difference')
print('3)Multiply')
print('4)Divide')

print('Enter variables')
x1 = input('Enter x1 --->')
x2 = input('Enter x2 --->')


proc = int(input('Enter proces -->'))

calculator = Calculator(x1, x2)

if proc == 1:
    calculator.sum(x1, x2)
elif proc == 2:
    calculator.differ(x1, x2)
elif proc == 3:
    calculator.mult(x1, x2)
elif proc == 4:
    calculator.divide(x1, x2)
else:
    print('There is no such action')