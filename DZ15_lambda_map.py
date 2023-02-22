orders_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

result = list(map(lambda i: (i[0], i[1], i[3] + 10 if i[3] * i[2] < 100 else i[3], i[2], i[2] * i[3]), orders_list))

print(result)


# Уявіть собі бухгалтерську книгу у книгарні. У цій книзі зберігаються записи про номер замовлення, назву книги,
# кількість і вартість однієї книги, як представлено нижче, в таблиці.
# Напишіть програму на Python, яка на вхід отримує список списків:
#
# [
#     [34587, 'Learning Python, Mark Lutz', 4, 40.95],
#     [98762, 'Programming Python, Mark Lutz', 5, 56.80],
#     [77226, 'Head First Python, Paul Barry', 3, 32.95],
#     [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
# ]
#
# та повертає список кортежів. Кожен кортеж складається з номера замовлення та назвы твору, ціни за товар та кількость.
# Вартість товару повинна бути збільшена на $10, якщо вартість замовлення менша за $100.
#
# Рекомендовано використовувати lambda та map.
