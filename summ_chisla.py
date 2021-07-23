

def summ(a = int(input("Введите трехзначное число: "))):

    b = a % 10
    a = a // 10
    d = a % 10
    a = a // 10
    return f"Сумма трех чисел равна: {a + d + b}"

print(summ())

