import sys
digit_string = sys.argv[1]

result = 0

for letter in digit_string:
    result+=int(letter)

print(result)