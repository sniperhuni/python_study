
lines = ['Hello.\n', 'Python\n', 'World.\n']

with open('hello.txt', 'w') as f:

    f.writelines(lines)


with open('hello.txt', 'r') as f:

    #f2 = f
    #a, b, c = f2
    #print('a', a.strip('\n'), 'b', b, 'c',c)

    for line in f:
        print(line.strip('\n'))
