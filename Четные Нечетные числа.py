chislo = input("Введите число: ")

a = len(chislo)
chetnie = 0
nechetnie = 0
b = 0
while a > 0:
    cifra = int(chislo[b]) % 2
    b += 1
    a -= 1
    if cifra == 0:
        chetnie += 1
    else:
        nechetnie += 1

print(f"В заданном числе {chetnie} четных и {nechetnie} нечетных чисел/-ла")