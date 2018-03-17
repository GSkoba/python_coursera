from datetime import datetime

def get_seconds():
    return datetime.now().second

print(get_seconds())


def add(x:int, y:int) -> int:
    return x+y

print(add(1,2))
print(type(add('hello',' miss')))


def extender (source_list, extend_list):
    source_list.extend(extend_list)

values = [1,2,3]
extender(values,[4,5,6])
print(values)

def say(greeting, name):
    print('{} {}!'.format(greeting,name))

print(say('Hello','Kitty'))
print(say(name='Kitty',greeting='Hello'))

def greeting(greet = 'kek'):
    print('Hello {}'.format(greet))

greeting()

def append_one(iterable =[]):
    iterable.append(1)
    return iterable

print(append_one([1]))

print(append_one())
print(append_one())

print(append_one.__defaults__)

def printer(*args):
    print(type(args))

    for argument in args:
        print(argument)


printer(1,2,3,4,5,6)

name_list = ['John','Bill','Any']

printer(*name_list)

def printer(**kwargs):
    print(type(kwargs))
    for key,values in kwargs.items():
        print('{} - {}'.format(key,values))

printer(a=10,b=11)

playload = {
    'user_id':117,
    'feedback':{
        'subject':'Registration fields',
        'message':'There is no country for old man'
    }
}

printer(**playload)

def foo(*args,**kwargs):
    printer(*args)
    printer(**kwargs)

foo(*name_list,playload)
