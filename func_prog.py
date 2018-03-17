def caller(fucn,params):
    return fucn(*params)

def printer(name,origin):
    print('I\'m {} of {}!'.format(name,origin))


caller(printer,['Moana','Motunui'])

def get_multiplier():
    def inner(a,b):
        return a*b
    return inner


multiplier = get_multiplier()
print(multiplier(10,11))

print(multiplier.__defaults__)

def get_multiplier(number):
    def inner(a):
        return a*number
    return inner

multiplier_by_2 = get_multiplier(2)
print(multiplier_by_2(10))