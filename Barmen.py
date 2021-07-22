class Naslednik:
    def nazvanie(self):
        return a + b + c + d + f

class Napitok_1(Naslednik):
    def nap(self):
        a = "Tekila"

class Napitok_2(Naslednik):
    def nap(self):
        b = "Vodka"

class Napitok_3(Naslednik):
    def nap(self):
        c = "Rom"

class Napitok_4(Naslednik):
    def nap(self):
        d = "Jin"

class Napitok_5(Naslednik):
    def nap(self):
        f = "Sirop"

n = Naslednik()

print(n.nazvanie())

