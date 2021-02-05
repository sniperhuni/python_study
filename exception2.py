'''
Try Else Finally

Finally: Regardless of the exceptions, a code will always be executed

'''

try:
     x = int(input('Put a number: '))
     y = 10/x

except ZeroDivisionError:
    print('Cannot divide by zero')

else:
    print(y)

finally:
    print('Codes were excuted')
