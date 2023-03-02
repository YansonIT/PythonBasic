s = input("Enter")

def hash_tag_creator(s):
    while not s:
        s = input("Введіть непорожню стрічку: ")
    words = s.split()
    hash_tag = '#'
    for word in words:
        hash_tag += word.capitalize()
    if len(hash_tag) > 140:
        return False
    return hash_tag

hash_tag_creator(s=s)
result = hash_tag_creator(s)
print(result)



#
# # Команда маркетингу витрачає занадто агато часу на введення хештегів.
#
# Давайте допоможемо їм за допомогою нашого власного генератора хештегів!
#
#
#
# Ось умови роботи функції:
#
# Він повинен починатися з хештегу (#).
# Усі слова мають мати першу літеру з великої літери.
# Якщо кінцевий результат довший за 140 символів, він має повернути false.
# Якщо вхід або результат є порожнім рядком, він повинен повернути помилку.
# Приклад:
#
# hash_tag_creator(" Hello there thanks for trying my Kata")   # повинно повернути  "#HelloThereThanksForTryingMyKata"
# hash_tag_creator(""  Hello   World  ")   # повинно повернути  "#HelloWorld"
# hash_tag_creator(""")  # повинно повернути exception