a = int(input("Введите трехзначное число: "))
b = a % 10
a = a // 10
d = a % 10
a = a // 10
e = a + d + b

print("Сумма введенного числа равна: ", e)
input("End")

