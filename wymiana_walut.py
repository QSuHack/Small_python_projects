import requests
# import xml.etree.ElementTree as et

print("Wybierz walutę: ")
url = "http://api.nbp.pl/api/exchangerates/tables/A/"
request = requests.get(url)
request = request.json()
request = request[0]
rates = request.get('rates')
codes = {}
for x in range(0, len(rates)):
    a = rates[x]
    codes[a.get("code")] = a.get("mid")
print("Dostępne waluty to: ")
for k in codes.keys():
    print(k, end=" ")
print("\n PLN ")
code = input("Pierwszy symbol(inny niż PLN)")
assert code != "PLN", "Błędne dane"

code2 = input("Drugi symbol: ")
print("Podaj typ: ", code2, '/', code, "-> 0 ", code, '/', code2, " -> 1")
conversion_type = input()
amount = float(input("Podaj wartosc: "))
m = codes.get(code)
flag = True
if code2 == 'PLN' :
    flag = False
if flag:
    n = codes.get(code)
    one = amount * (1 / m)
    if conversion_type:
        print(one*n, code2)
    else:
        print(one*(1/n), code2)
else:
    if conversion_type:
        print(amount * m, code2)
    else:
        print(amount * (1 / m), code)
