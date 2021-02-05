y = [10, 20, 30]

try:
    index, x = map(int, input('Put an index and a number: ').split())
    print(y[index] / x)

except ZeroDivisionError as e:
    print('Cannot divide by zero, ', e)

except IndexError as e:
    print('wrong index, ', e)
