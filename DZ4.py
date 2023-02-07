# Обернуты число

num = int(input("Enter number:  "))

first = int(num % 10)
second = int(num /10 % 10)
third = int(num / 100 % 10)

  # Перевірка
print(first)
print(second)
print(third)
print(type(first), type(second), type(third))


print("result :", third + second * 10 + first * 100)
