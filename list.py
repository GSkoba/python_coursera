empty_list = []
empty_list = list()

none_list = [None]*10

collections = ['list','tuple','dict','set']

user_data = [
    ['Elena',4.4],
    ['Andrey', 4.2]
]

len(collections)

print(collections)

print(collections[0])

print(collections[-1])

print('tuple' in collections)

range_list = list(range(10))
print(range_list)

print(range_list[1:3])

print(range_list[::2])

print(range_list[::-1])

for collection in collections:
    print('Learnin {} ...'.format(collection))

for idx,collection in enumerate(collections):
    print('#{} {}'.format(idx,collection))

collections.append('new')
print(collections)

collections.extend(['new1','new2','new3'])
print(collections)

del collections[4]
print(collections)

numbers = range(20)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

tag_list = ['python','course']

print(', '.join(tag_list))

import random

numbers = []

for _ in range(10):
    numbers.append(random.randint(1,20))

print(numbers)

print(sorted(numbers))
print(numbers)
numbers.sort(reverse=True)
print(numbers)