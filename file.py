file = open('hello.txt', 'w')
file.write('Hello, world!!')
file.close()

'''
The file will be automatically closed
'''
with open('hello.txt', 'r') as f:
    s = f.read()
    print(s)
