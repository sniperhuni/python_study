
try:
    x = int(input('Put a multiple of 3: '))
    if x%3 !=0:
        raise Exception('This is not a multiple of 3')

    print(x)

except Exception as e:
    print('exception has been occurred,', e)
