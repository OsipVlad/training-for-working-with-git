def f(a):
    if a == a[::-1]:
        return True
    return False
print(f("abbat"))