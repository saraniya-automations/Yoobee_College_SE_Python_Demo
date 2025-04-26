x = input('Input a number to find factorial: ')
x = int(x)

if x >= 0:
    factorial = 1  
    for i in range(1, x + 1):
        factorial *= i
    print('Factorial of', x, 'is:', factorial)
else:
    print('Unable to find the factorial of a negative number.')
