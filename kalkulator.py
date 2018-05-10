def dodawanie():
    a = raw_input("Pierwsza liczba ")
    b = raw_input("Druga liczba ")
    wynik = float(a) + float(b)
    return wynik


def odejmowanie():
    a = raw_input("Pierwsza liczba ")
    b = raw_input("Druga liczba ")
    wynik = float(a) - float(b)
    return wynik


def mnozenie():
    a = raw_input("Pierwsza liczba ")
    b = raw_input("Druga liczba ")
    wynik = float(a) * float(b)
    return wynik


def dzielenie():
    a = raw_input("Pierwsza liczba ")
    b = raw_input("Druga liczba ")
    wynik = float(a) / float(b)
    return wynik


def dzieleniecal():
    a = raw_input("Pierwsza liczba ")
    b = raw_input("Druga liczba ")
    dziel = int(a) / int(b)
    reszta = int(a) % int(b)
    wynik = "wynik", dziel, "reszty", reszta
    return wynik


def potegowanie():
    a = raw_input("Liczba ")
    b = raw_input("Potęga ")
    wynik = float(a) ** float(b)
    return wynik