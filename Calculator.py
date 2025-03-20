print("----Simple Calculator----")
#user inputs first number, operator and second number
print("Enter first number: ")
num1 = float(input())
print("Enter operator (+, -, *, /): ")
operator = input()
print("Enter second number: ")
num2 = float(input())
#checks the operator and performs the operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    
#checks if the second number is zero
    if num2 == 0:
        print("Error: Division by zero!")
        exit()
    result = num1 / num2
else:
    print("Invalid operator")
    exit()
#displays the result
print(f"{num1} {operator} {num2} = {result}")