# We Are making  a simple  claculator #

print()
print('C A L C U L A T O R')
print()
print('Operator     Instructions')
print('')
print('+ = Addition')
print('- = Subtract')
print('* =  Multiply')
print('/ =  Divide')
print('** = Raise to the power')
print('// = Quotient')
print('% =  Remainder')
print()

a = int(input('Enter first Number:- '))
print()
op = (input('Enter Operator(+,-,*,/,//,**,%)=> '))
print()
b = int(input('Enter second Number:- '))
print()
Result = 0
if op == '+':
    Result = a + b
    print(Result, 'Is the sum of two numbers')
elif op == '-':
    Result = a - b
    print(Result, 'Is the subtraction  of two numbers')
elif op == '*':
    Result = a * b
    print(Result, 'Is the Multiplication of two numbers')
elif op == '/':
    Result = a / b
    print(Result, 'Is the Division  of two numbers')
elif op == '**':
    Result = a ** b
    print(a, 'Raise to the Power', b, 'Is', Result)
elif op == '//':
    Result = a // b
    print(Result, 'Is the Quotient')
elif op == '%':
    Result = a % b
    print(Result, 'Is the Remainder  of two numbers')
else:
    print('The Operator is wrong')
