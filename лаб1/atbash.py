

alpha = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я"
alpha = alpha.split()
alpha.append(' ')
cypher = alpha.copy()
cypher.reverse()


print(alpha)
print(cypher)

while True:
    finish = str(input("Предложение, которое будет зашифровано с помощью шифра Цезаря (f - для завершения работы программы): "))
    if finish == 'f':
        break

    cypher_mess = str()
    for symbol in finish:
        cypher_mess += cypher[alpha.index(symbol)]

    print(cypher_mess)



