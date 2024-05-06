"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martin Pokorný
email: pokornymartin2@gmail.com
discord: martin_pokorny86
"""
import random

oddelovac = "-" * 35

print("Zdravím vás!")
print(oddelovac)
print(f"Bylo vygenerováno 4místné číslo.\nZahrajme si hru Bulls & Cows.")
print(oddelovac)

def generator_nahodnych_cisel():
    """
    Vytvoří tajné 4místné číslo, které je unikátní a nesmí začínat 0
    """
    while True:
        # vygenerujeme 4místné náhodné číslo a převedeme na string kvůli procházení všech čísel
        utajene_cislo = str(random.randint(1000,9999))
        # zajistíme, aby všechna vygenerovaná čísla byla jedinečná
        if len(set(utajene_cislo)) == 4:
            break
    return utajene_cislo

utajene_cislo = generator_nahodnych_cisel()

def hrac():
    """
    Uživatel zadá 4místné unikátní číslo, které nezačíná nulou
    """
    print(oddelovac)
    while True:
        cislo_hrace = input(f"Zadejte číslo:\n{oddelovac}\n>>> ")
        if not cislo_hrace.isdigit():
            print("Zadejte pouze číselné hodnoty")
            continue
        elif len(cislo_hrace) != 4:
            print("Zadané číslo nemá 4 znaky")
            continue
        elif cislo_hrace[0] == '0':
            print("Číslo nesmí začínat nulou")
            continue
        elif len(set(cislo_hrace)) != len(cislo_hrace):
            print("Zadané číslo obsahuje duplicity")
            continue
        break
    return cislo_hrace # díky return se cislo_hrace stane výstupem fce

def vyhodnoceni (utajene_cislo, cislo_hrace):
    bulls = sum(a == b for a, b in zip(utajene_cislo, cislo_hrace))
    cows = sum(a in utajene_cislo for a in cislo_hrace) - bulls
    return bulls, cows

pokus = 0

while True:
    pokus += 1
    cislo_hrace = hrac()
    bulls, cows = vyhodnoceni(utajene_cislo, cislo_hrace)
    if bulls == 4:
        print("Gratulujeme, uhodl jste správné pořadí všech čísel. Počet pokusů:", pokus)
        break
    else:
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
