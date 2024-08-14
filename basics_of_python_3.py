# FUNCTIONS AND LOOPS
# Defining Functions:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# For Loops:
for i in range(1, 6):
    print(i)
# If - Else Statements:
x = 10
if x > 0:
    print('Positive')
elif x < 0:
    print('Negative')
else:
    print('Zero')