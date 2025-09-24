class Calculator_operations():
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation

    def calculator(self):
        if self.operation == "add" or self.operation == "+":
            return self.a + self.b
        elif self.operation == "sub" or self.operation == "-":
            return self.a - self.b
        elif self.operation == "mul" or self.operation == "*":
            return self.a * self.b
        elif self.operation == "div" or self.operation == "/":
            if self.b == 0:
                return "division not possible"
            else:
                return self.a / self.b
        else:
            return "Invalid operation"


a = float(input("Enter 'a' value: "))
b = float(input("Enter 'b' value: "))
operation = input("Enter operations like (add/sub/mul/div or + - * /): ")

calc = Calculator_operations(a, b, operation)
print("output =", calc.calculator())

'''if a = 12 & b = 5 & operation= *
then Output = 60.0  '''
