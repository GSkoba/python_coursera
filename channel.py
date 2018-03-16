company = "my.com"
if "my" in company:
    print("Условие выполнено!")

company = "example.net"
if "my" in company or company.endswith(".net"):
    print("Условие выполнено!")

company = "google.com"
if "my" in company:
    print("Условие выполнено!")
else:
    print("Условие не выполнено!")

if "my" in company:
    print("Подстрока my найдена")
elif "google" in company:
    print("Подстрока google найдена")
else:
    print("Подстрока google не найдена")

score_1 = 5
score_2 = 0
winner = "Argentina" if score_1>score_2 else "Jamaica"
print(winner)

i = 0
while i < 100:
    i += 1
print(i)

name = "Alex"
for letter in name:
    print(letter)

for i in range(3):
    print(i)

result = 0
for i in range(101):
    result+=i
print(result)

for i in range(5,8):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(101):
    pass

result = 0
while True:
    result+=1
    if result >= 100:
        break

print(result)