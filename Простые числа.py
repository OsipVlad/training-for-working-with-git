a = int(input("Введите число: "))

for n in range(2, a + 1):
    if (a % n) == 0:
        print("False")
        break
    elif (a % n) > 0:
        print("True")
        break