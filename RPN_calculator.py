import math


class AllDone(Exception): pass


def oblicz(znak_dzialania, lista):
        try:
            if znak_dzialania == '+':
                lista.append(lista.pop() + lista.pop())
                print(lista[-1])
            elif znak_dzialania == "-":
                a = lista.pop()
                b = lista.pop()
                lista.append(b-a)
                print(lista[-1])
            elif znak_dzialania == "/":
                a = lista.pop()
                b = lista.pop()
                lista.append(b/a)
                print(lista[-1])
            elif znak_dzialania == "*":
                lista.append(lista.pop() * lista.pop())
                print(lista[-1])
            elif znak_dzialania == "sqrt":
                lista.append(math.sqrt(lista.pop()))
                print(lista[-1])
            elif znak_dzialania == "pow":
                a = lista.pop()
                b = lista.pop()
                lista.append(b ** a)
                print(lista[-1])
            elif znak_dzialania.isspace() or znak_dzialania == "":
                pass
            elif znak_dzialania == "exit":
                raise AllDone
            else:
                print("Nieznana operacja!")
        except IndexError:
            print("Pusty stos!")


listx = []
__doc__ = """
Kalkulator o odwróconej notacji polskiej (ang. reverse Polish notation (RPN/ONP)) 
Tryb oddzielenia nową linią: 0
Tryb odzielenia spacją : 1
Dostępne funkcje:
+ dodawanie 
- odejmowanie 
* mnożenie
/ dzielenie rzeczywiste
sqrt pierwiastkowanie kwadratowe
pow potęgowanie
exit wyjście
"""
print(__doc__)
try:
    if not int(input()):
        while True:
            znak = input()
            try:
                liczba = int(znak)
                listx.append(liczba)
            except ValueError:
                oblicz(znak, listx)
    else:
        while True:
            znak = input().split(" ")
            for el in znak:
                try:
                    liczba = int(el)
                    listx.append(liczba)
                except ValueError:
                    oblicz(el, listx)
except AllDone:
    pass
