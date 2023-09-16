import sys

alpha = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я"
alpha = alpha.split()
password = list(input("Пароль: ").lower())
k = int(input("Сдвиг: "))
k = k % len(alpha)


uniq_letters = list()
for letter in alpha:
    if letter not in password:
        uniq_letters.append(letter)
if k == 0:
    cypher = password + uniq_letters
elif k <= len(alpha) - len(password):
    cypher = uniq_letters[-k:] + password + uniq_letters[:len(uniq_letters)-k]


print(alpha)
print(cypher)

while True:
    mess = str(input("Предложение, которое будет зашифровано с помощью шифра Цезаря (f - для завершения работы программы): "))
    if mess == 'f':
        break

    cypher_mess = str()
    for symbol in mess:
        if symbol == ' ':
            cypher_mess += ' '
        else:
            cypher_mess += cypher[alpha.index(symbol)]

    print(cypher_mess)