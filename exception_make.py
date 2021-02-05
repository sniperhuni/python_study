class NotThreeMultipleError(Exception):

    def __init__(self):
        super().__init__('This is not a multiple of 3')

def three_multiple():
    try:
        x = int(input('Put a multiple of 3: '))

        if x%3 !=0:
            raise NotThreeMultipleError
        print(x)

    except Exception as e:
        print('Exception has been occurred.' , e)

three_multiple()
