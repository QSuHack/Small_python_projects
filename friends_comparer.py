import json
import os
import time
filename1 = input("Podaj nazwę starszego pliku") + ".json"
if filename1 ==".json":
    filename1 = "friends.json"
filename2 = input("Podaj nazwę nowszego pliku") + ".json"
if filename2 == ".json":
    filename2 = "friends2.json"
file1 = json.load(open(filename1))["friends_v2"]
file2 = json.load(open(filename2))["friends_v2"]
missing_people, new_friends = 0,0
for key in file1:
    if key not in file2:
        print(f"Znaleziono brakującą osobę: {key.get('name').encode('iso-8859-1').decode('utf-8')}")
        print(f"Dodano o {time.ctime(key.get('timestamp'))}")
        missing_people +=1
for key in file2:
    if key not in file1:
        print(f"Znaleziono nową osobę: {key.get('name').encode('iso-8859-1').decode('utf-8')} ")
        print(f"Dodano o {time.ctime(key.get('timestamp'))}")
        new_friends +=1
print(f"Zgubione osoby: {missing_people}")
print(f"Nowe osoby: {new_friends}")
friends_number = len(file1)
new_friends_number = len(file2)
print(f"Masz {new_friends_number} znajomych, to zmiana o: {new_friends_number -friends_number} ")