class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        positive = (a < 0) == (b < 0) 
        a, b = abs(a), abs(b)
        for _ in range(b):
            result = self.add(result, a)
        return result if positive else -result

    def divide(self, a, b):
        if b == 0: return "Error: Division by zero"
        result = 0
        positive = (a < 0) == (b < 0) 
        a, b = abs(a), abs(b)
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result if positive else -result
    
    def modulo(self, a, b):
        if b == 0: return "Error: Modulo by zero"
        negative = a < 0
        a, b = abs(a), abs(b)
        while a >= b:
            a = self.subtract(a, b)
        return -a if negative else a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))