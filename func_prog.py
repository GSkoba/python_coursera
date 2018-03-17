def caller(fucn, params):
    return fucn(*params)


def printer(name, origin):
    print('I\'m {} of {}!'.format(name, origin))


caller(printer, ['Moana', 'Motunui'])


def get_multiplier():
    def inner(a, b):
        return a * b

    return inner


multiplier = get_multiplier()
print(multiplier(10, 11))

print(multiplier.__defaults__)


def get_multiplier(number):
    def inner(a):
        return a * number

    return inner


multiplier_by_2 = get_multiplier(2)
print(multiplier_by_2(10))


def squarify(a):
    return a ** 2


print(list(map(squarify, range(5))))


def is_positive(a):
    return a > 0


print(list(filter(is_positive, range(-2, 3))))

print(list(map(lambda x: x ** 2, range(5))))

print(list(filter(lambda x: x % 2 == 0, range(-10, 10))))

print(list(map(lambda x: str(x), range(-10, 10))))


def stringify_list(num_list):
    return list(map(str, num_list))


print(stringify_list(range(10)))

from functools import reduce


def multiply(a, b):
    return a * b


print(reduce(multiply, [1, 2, 3, 4, 5]))

from functools import partial


def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)


hier = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hello')

print(hier('brother'))
print(helloer('sir'))

squere_list = [number ** 2 for number in range(10)]
print(squere_list)

even_list = [num for num in range(10) if num % 2 == 0]
print(even_list)

squere_map = {number: number**2 for number in range(5)}
print(squere_map)

reminders_set = {num % 10 for num in range(100)}
print(reminders_set)

num_list = range(10)
squere_list = [x**2 for x in range(5)]

print(list(zip(num_list,squere_list)))

print(list(zip(filter(bool,range(3)),[x for x in range(3) if x])))