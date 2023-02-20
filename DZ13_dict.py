d = {
  'apple': ['malum', 'pomum', 'popula'],
  'fruit': ['baca', 'bacca', 'popum'],
  'punishment': ['malum', 'multa']
}

new_dict = {}

for key in d:
    for value in d[key]:
        if value not in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)


print(new_dict)


# Даний словник ключами якого є англійські слова, а значення списки латинських слів. Потрібно розгорнути словник.
# Іншими словами, необхідно, на підставі заданого словника, створити новий словник, у якого як ключі будуть взяті
# латинські слова, з першого словника, а значеннями будуть англійські слова, що відповідають їм.
#
#
#
# Вихідний словник:
#
#
#
# d = {
#   'apple': ['malum', 'pomum', 'popula'],
#   'fruit': ['baca', 'bacca', 'popum'],
#   'punishment': ['malum', 'multa']
# }