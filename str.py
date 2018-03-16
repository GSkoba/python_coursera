example_str = "Python is cool"
print(example_str)
print(type(example_str))

example_str = 'Mail and odnoklassniki is "very" cool'
print(example_str)

example_str = "Hello \"Helo\""
print(example_str)

example_str = "c:\\\\"
print(example_str)

#Сырые строки
example_str = r"c:\\"
print(example_str)

#Оператор \
example_str = "Fffffffffffffffffffffffff" \
    "fffffffffffffffffffffffffffffffffffffff"\
    "fffffffffffffffffffffffffffffffffffffff"
print(example_str)

#Оператор """
example_str = """
    Ghbdfffffffffffffffffffffffffffffffffd
dffffffffffffffffffffffffffffffffff
dffffffffffffffffffffffffff
dfdfdfdf

fdfdfdf

"""
print(example_str)

example_str = "Можно складывать " + "строки"
print(example_str)

example_str = "Даже можно умножать!"*3
print(example_str)

#Адресс в памяти можно запросить с помощью оператора id
print(id(example_str))

#Срезать строку [start:stop:step]
example_str="Курс про Python на Coursera"
print(example_str[9:])
print(example_str[9:15])
print(example_str[-8:])

example_str = "0123456789"
print(example_str[::2])
print(example_str[::-1])

#Методы строк
#count
example_str = "Cool, hello from my heart"
print(example_str.count("o"))

#capitalize - первая буква в строке заглавная
example_str = "спб"
print(example_str.capitalize())

#isdigit
example_str = "2017"
print(example_str.isdigit())


#Оператор in
print("3.14" in "Пи = 3.14")

example_str = "Привет"
for letter in example_str:
    print("Letter ",letter)

template = "%s - главное достоинство программистов. (%s)"
print(template % ('Лень', 'Larry Wall'))
print(template)

template = "{} не лгут, но {} используются формулами. ({})".format("Цифры", "лжецы", "Robert A.Heinlein")
print(template)

template = "{num} Кб должно хватить для любых задача. ({author})".format(num  = 640, author ="Bill Gates")
print(template)

author = "Donald Knuth"
subject = "оптимизация"

template = f"Преждевременая {subject} - корень всех зол. ({author})"
print(template)

num = 8
template = f"Binary: {num:#b}"
print(template)
num2 = 15
print(f"Binary: {num2:#b}")

num3 = 2/3
print(num3)
print(f"{num3:.3f}")

#name = input("Write your name:")
#print(f"Hello, {name}!")

example_byte = b"hello"
print(example_byte, type(example_byte))

for element in example_byte:
    print(element)

example_string = "привет"
print(example_string, type(example_string))

encoded_string = example_string.encode(encoding="utf-8")
print(encoded_string, type(encoded_string))
decoded_string = encoded_string.decode()
print(decoded_string)
print(r"//\\")
encoded_string = "првиет"
print(encoded_string[:])