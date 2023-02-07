num = int(input("Enter an integer: "))
# num_list = []
inputs = 0
sum = 0
even_nom = 0
not_even_nom = 0

while num != 0:
    if num != 0:
        inputs += 1                # Количество вводов
    if num !=0:
        sum += int(num)            # Сумирование
    if num % 2 == 0:
        even_nom += 1              # Количество четных
    if num % 2 != 0:
        not_even_nom += 1          # Количество  не четных
    num = int(input("Enter an integer: "))
    if num == 0:
        print("\n---- Mission Complete---- \n")
print("Total integers entered :", inputs)
print("Sum of all entered numbers :", sum)
print("Average", sum / inputs)
print("Even nom: ", even_nom)2
print("Not even nom: ", not_even_nom)

# Програма запитує введення, з клавіатури, цілі числа, поки не буде введено 0.
# Як тільки буде введено 0 (нуль), програма повинна порахувати та вивести на екран:
#
# -кількість введених чисел (завершальний 0 не рахується)
# -їхню суму
# -середнє арифметичне всіх введених чисел (за винятком завершального числа 0)
# -визначити максимальне та мінімальне значення
# -визначити кількість парних та непарних елементів у послідовності