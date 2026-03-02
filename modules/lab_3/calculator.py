from typing import Optional, Any
from math import exp, tan

Num_type = int | float

class Calculator:
    def calculate(self) -> Optional[Num_type]:
        while True:
            number_a, number_b = 0.0, 0.0

            selected_operation = input(
                        "[+, -, *, /, **, //, %, !, tan, exp]\n"
                        "Input operation: ")
        
            if selected_operation == "exit":
                print("Exiting the calculator.")
                break
            elif selected_operation not in ('+', '-', '*', '/', '**', '//', '%', '!', 'tan', 'exp'):
                print("Error: Invalid operation. Please try again.")
                continue
            

            # Унарні операції
            if selected_operation in ["!", "tan", "exp"]:
                number_a = input("Enter the number: ")

                try:
                    number_a = float(number_a)
                except ValueError:
                    if number_a.lower() == "exit": 
                        print("Exiting the calculator.")
                        break
                    print("Error: Invalid input. Please enter a valid number.")
                    continue

            # Бінарні операції
            else:
                try:
                    number_a = input("Enter the first number: ")
                    number_a = float(number_a)

                    number_b = input("Enter the second number: ")
                    number_b = float(number_b)
                except ValueError:
                    if (str(number_a).lower() == "exit" or str(number_b).lower() == "exit"):
                        print("Exiting the calculator.")
                        break
                    print("Error: Invalid input. Please enter a valid number.")
                    continue
            

            match selected_operation:
                case "+":
                    number_a = self.add(number_a, number_b)
                    print(number_a)
                case "-":
                    number_a = self.subtract(number_a, number_b)
                    print(number_a)
                case "*":
                    number_a = self.multiply(number_a, number_b)
                    print(number_a)
                case "/":
                    if number_b == 0:
                        print("Can't divide on 0")
                        continue
                    number_a = self.divide(number_a, number_b)
                    print(number_a)
                case "**":
                    number_a = self.exponentiate(number_a, number_b)  
                    print(number_a)
                case "%":
                    if number_b == 0:
                        print("Can't divide on 0")
                        continue
                    number_a = self.modulus(number_a, number_b)
                    print(number_a)
                case "//":
                    if number_b == 0:
                        print("Can't divide on 0")
                        continue
                    number_a = self.floor_divide(number_a, number_b)
                    print(number_a)
                case "!":
                    if number_a < 0:
                        print("Can't calculate factorial of a negative number.")
                        continue
                    number_a =self.factorial(int(number_a))
                    print(number_a)
                case "tan":
                    number_a = tan(number_a) 
                    print(number_a)
                case "exp":
                    number_a = exp(number_a) 
                    print(number_a)
                case _:
                    print("Error: Invalid operation. Please try again.")

        return number_a if isinstance(number_a, (int, float)) else None


    def add(self, a: Num_type, b: Num_type) -> Num_type:
        return a + b
    

    def multiply(self, a: Num_type, b: Num_type) -> Num_type:
        return a * b
    
    
    def divide(self, a: Num_type, b: Num_type) -> Num_type:
        return a / b
    

    def subtract(self, a: Num_type, b: Num_type) -> Num_type:
        return a - b
    

    def exponentiate(self, a: Num_type, b: Num_type) -> Num_type:
        return a ** b
    

    def modulus(self, a: Num_type, b: Num_type) -> Num_type:
        return a % b
    

    def floor_divide(self, a: Num_type, b: Num_type) -> Num_type:
        return a // b
    

    def factorial(self, a: Num_type) -> Num_type:
        if (a == 0 or a == 1):
            return 1
        
        total = 1
        while (a > 1):
            total *= a
            a -= 1

        return total
    


if __name__ == "__main__":
    C = Calculator()
    res = C.calculate()