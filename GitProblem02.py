# Ask user for two numbers and compare. Display message when 1st number is greater
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num1 > num2:
    print('Number 1 is bigger than Number 2')
elif num1 < num2:
    print('Number 2 is bigger than Number 1')
else:
    print('Number 1 is equal to Number 2')