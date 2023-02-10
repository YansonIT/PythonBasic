s = input("Введіть рядок:")
ch = input("Введіть символ:")
step = 0


while True:
    if step == 0:
        print(s.find(ch))
        step = (step + s.find(ch))
    if (s.find(ch, step + 1, )) >= 0:
        print(s.find(ch, step + 1, ))
        step = (s.find(ch, step + 1, ))
    if (s.find(ch, step + 1, )) == -1:
        break



'''Користувач вводить окремо рядок `s` і один символ `ch`. 

Необхідно здійснити пошук у рядку `s` всіх символів `ch`.

s = input("Введіть рядок:")
ch = input("Введіть символ:")


Треба вивести всі індекси символа у введеному рядку.

Для вирішення потрібно використовувати тільки функцію `find()`

(rfind()), оператори `if` і `for`(while).'''

