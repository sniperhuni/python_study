
def three_multiple():
    x = int(input('Put a multiple of 3: '))

    if x%3 !=0:
        raise Exception('This is not a multiple of 3')

        '''
        Because there is not 'except' in the function,
        an exception will be passed into the outside of the block
        '''

    print(x)

try:
    three_multiple()
except Exception as e:
    print('Exception has been occurred.' , e)
    
