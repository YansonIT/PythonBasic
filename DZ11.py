import random

my_l = []
k = int(input("Enter index  :"))

for i in range(10):
    my_l.append(random.randint(1, 10))

print(my_l)

my_l = my_l[0:k] + my_l[k + 1:] + my_l[k : k + 1]

print("Змінений список :",my_l)
my_l.pop()
print("Змінений список з видаленим елементом :",my_l)

# Дано список із чисел та індекс елемента у списку `k`. Видаліть зі списку елемент з індексом `k`,
# зрушивши вліво всі елементи, що стоять правіше елемента з індексом `k`.
#
#
#
# a). Програма отримує на вхід перелік, потім число `k`. Програма зсуває всі елементи,
# а потім видаляє останній елемент списку за допомогою методу `pop()` без параметрів.
#
# b). Програма повинна здійснювати зсув безпосередньо у списку, а не робити це під час виведення
# елементів. Також не можна використовувати додатковий перелік.
#
# c). Також не слід використовувати метод `pop(k)` із параметром.
#
# d). Використати оператор del НЕ МОЖНА!