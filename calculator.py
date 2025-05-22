#Home Work - no. 1

class calculator:
    brand = "casio"
    def add(self, num1, num2):
        result = num1 + num2
        print(f'The resilt is: {result}')
    def deduct(self, num1, num2):
        result = num1 - num2
        print(f'The resilt is: {result}')
    def multiply(self, num1, num2):
        result = num1 * num2
        print(f'The resilt is: {result}')
    def Divide(self, num1, num2):
        result = num1 / num2
        print(f'The resilt is: {result}')

calculate = calculator()
calculate.add(12,20)
calculate.deduct(12,20)
calculate.multiply(12,20)
calculate.Divide(12,20)