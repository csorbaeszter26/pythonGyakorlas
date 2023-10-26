def elso():
    szam = 0
    while szam <= 150:
        if szam % 2 == 0:
            print(szam, end=", ")
        szam += 1
    print(150, end="")

def masodik():
    szam=0
    while szam < 5:
        szam += 1
        szamok = int(input("Adjon meg egy számot!"))
        if szamok % 3 == 0:
            print(szamok)

def harmadik():
    szam = (int(input("Kérem adjon meg egy számot!")))
    while not szam % 10 == 0:
        szam = (int(input("Kérem adjon meg egy számot!")))
    print("Ez a szám oszttható 10-el!")

def negyedik():
    szam = (int(input("Kérem adjon meg egy számot!")))
    while not ((szam > 9) and (szam < 100) and (szam % 2 == 0)):
        szam = (int(input("Kérem adjon meg egy számot!")))
    print("Ez a szám kétjegyű és páros!")

def otodik():
    szam = (int(input("Kérem adjon meg egy számot!")))
    while not ((szam > 0) and (szam % 2 == 1)):
        szam = (int(input("Kérem adjon meg egy számot!")))
    print("Ez a szám pozitív és páratlan!")

def hatodik():
    import math

    szam = (int(input("Kérem adjon meg egy számot!")))
    while not ((szam % 3 == 0) or (round(math.sqrt(szam)) ==(math.sqrt(szam)))):
        szam = (int(input("Kérem adjon meg egy számot!")))
    print("Ez a szám 3-mal osztható vagy négyzetszám!")

def hetedik():
    a = (int(input("Kérem adjon meg egy számot!")))
    b = (int(input("Kérem adjon meg egy számot!")))
    c = (int(input("Kérem adjon meg egy számot!")))
    while not ((a + b > c) and (a + c > b) and (c + b > a)):
        a = (int(input("Kérem adjon meg egy számot!")))
        b = (int(input("Kérem adjon meg egy számot!")))
        c = (int(input("Kérem adjon meg egy számot!")))
    print("Szerkeszthető háromszög oldalait kaptuk ezekből a számokból!")

def nyolcadik():
    szoveg = str(input("Kérem adjon meg egy szöveget"))
    while not (len(szoveg) > 2):
        szoveg = str(input("Kérem adjon meg egy szöveget"))
    print("A szöveg legalább 3 karakteres: " + szoveg.upper())

def kilencedik():
    szoveg = str(input("Kérem adjon meg egy szöveget"))
    while not ((len(szoveg) > 3) and (szoveg == szoveg.lower())):
        szoveg = str(input("Kérem adjon meg egy szöveget"))
    print("A szöveg legalább 4 karakteres és kis betűs: " + szoveg)

def tizedik():
    szam = (int(input("Kérem adjon meg egy számot! Hogy ha ki akar lépni, írjon 0-t.")))
    eredmeny = 0
    sorszam = 0
    while not (szam == 0):
        eredmeny += szam
        sorszam += 1
        atlag = eredmeny/sorszam
        szam = int(input("Kérem adjon meg egy számot! Hogy ha ki akar lépni, írjon 0-t."))
    print("A megadott számok átlaga: " + str(round(atlag, 2)))

def tizenegy():
    szam = (int(input("Kérem adjon meg egy pozitív számot! Hogy ha ki akar lépni, írjon 0-t.")))
    eredmeny = 0
    sorszam = 0
    while not (szam == 0):
        while szam < 0:
            szam = (int(input("A szám nem pozitív! Kérem adjon meg egy pozitív számot! Hogy ha ki akar lépni, írjon 0-t.")))
        eredmeny += szam
        sorszam += 1
        atlag = eredmeny / sorszam
        szam = int(input("Kérem adjon meg egy számot! Hogy ha ki akar lépni, írjon 0-t."))
    print("A megadott számok átlaga: " + str(round(atlag, 2)))

