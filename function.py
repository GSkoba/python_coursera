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

def greetin