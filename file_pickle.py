import pickle

name = 'james'
age = 17
address = 'montreal'
scores = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5}

'''
When we save object with pickle, use 'wb' (write in binary)
'''
with open('james.p', 'wb') as file:

    pickle.dump(name, file)
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(scores,file)


with open('james.p', 'rb') as f:

    name1 = pickle.load(f)
    age1 = pickle.load(f)
    address1 = pickle.load(f)
    scores1 = pickle.load(f)

    print(name1)
    print(age1)
    print(address1)
    print(scores1)
