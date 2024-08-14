# FUNCTIONS AND LOOPS
# Defining Functions:

print("Demonstrate a function:")


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(f'{i}! = {result}')
    return result


factorial(5)

print("\nDemonstrate a For loop:")
# For Loops:
for j in range(1, 6):
    print(j)

print("\nDemonstrate an if - else statement:")
# If - Else Statements:
x = -2
if x > 0:
    print(f'{x} is Positive')
elif x < 0:
    print(f'{x} is Negative')
else:
    print(f'{x} is Zero')
