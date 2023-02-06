# Обернуты число

num = int(input("Enter number:  "))

first  = num % 10
second = int(num /10 % 10)
third = int(num / 100 % 10)

# Перевірка
#print(first)
#print(second)
#print(third)

result = third + second * 10 + first * 100
print(result)
