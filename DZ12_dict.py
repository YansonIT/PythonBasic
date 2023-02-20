n_str = " I study Python I study C I study Java"
new_l = n_str.split()
new_dict = {}

new_dict = {}

for word in new_l:
    value = new_dict.get(word, 0)
    new_dict[word] = value + 1




# второй вариант
#
# for word in new_l :
#         new_dict[word] = new_l.count(word)

print(new_dict)



# У єдиному рядку записаний текст. Для кожного слова з цього тексту підрахуйте скільки разів воно зустрічалося в цьому тексті.
#
#
#
# Завдання необхідно вирішити з використанням словника.