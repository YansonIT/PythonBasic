while True:
    try:
        num = int(input("Введіть число : "))
        if num <= 0:
            raise ValueError("Помилка!!! Введіть число більше 0")
        break
    except ValueError as j:
        print("Помилка: ", j)

def number_collaps(num):
    if num <= 9:
        return num
    else:
        return number_collaps(sum(int(d) for d in str(num)))

result = number_collaps(num)
print(result)

