def addition(a,b):
    return a + b

addition(1,2)

def subtraction(a, b):
    return a - b

print("Addition result:", addition(1, 2))
print("Subtraction result:", subtraction(5, 3))

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Division result:", division(10, 2))