while True:
    try:
        num = int(input("Введіть число : "))
        if num <= 0:
            raise ValueError("Помилка!!! Введіть число быльше 0")
        break
    except ValueError as j:
        print("Помилка: ", j)

def expanded_form(num):
    digits = []
    n = 10 ** (len(str(num)) - 1)
    while num > 0:
        digit = (num // n) * n
        if digit > 0:
            digits.append(str(digit))
        num -= digit
        n //= 10
    print(" + ".join(digits))

expanded_form(num=num)
