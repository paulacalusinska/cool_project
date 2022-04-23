entries = []
from datetime import date

def dodaj(content, date_str):

    entry = {}
    entry["content"] = content
    entry["date"] = date_str
    entries.append(entry)

def get_date():
    data_wpisu = date.today()
    date_str = data_wpisu.strftime("%d/%m/%Y")
    return date_str


def czytaj():
    for wpisy in entries:
        print(wpisy)


while True:
    warunek = int(input("1 - dodaj 2 - czytaj 3 - wyjdź: "))
    if warunek == 1:
        content = input("Dodaj wpis: ")
        date_str = get_date()

        dodaj(content, date_str)
    if warunek == 2:
        czytaj()
    if warunek == 3:
        break

