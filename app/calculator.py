class Calculator(object):
    def add(self, num1, num2):
        sum = num1 + num2
        return sum
a = Calculator()
sum = a.add(2,2)
print(sum)