import random
import math

def elso(a:int, b:int):
    osszeg:int = 0
    for i in range (a, b, 1):
        if i % 2 == 0:
            osszeg+=i
    return osszeg

def masodik():
    b:int = 0
    for i in range(0, 20, 1):
        a:int = math.floor(random.random()*21-10)
        if a < 0:
            b+=1
    return b

def harmadik():
    a:int =0
    for i in range(0, 10, 1):
        b:int = math.floor(random.random()*22+12)
        a += b
    return a

def negyedik():
    max:int = 0
    for i in range(0, 8, 1):
        b:int = math.floor(random.random()*30+20)
        if b > max:
            max = b
    return max

def otodik():
    osszeg: int = 0
    for i in range(1, 4, 1):
        szam:int = int(input(f"Kérem a {i}. számot: "))
        osszeg += szam

    szamolas = osszeg / 3
    return szamolas

def hatodik():
    mennyiseg:int = 0
    osszeg:int = 0
    szam: int = int(input("Kérek egy számot: "))
    osszeg += szam

    while szam != 0:
        szam: int = int(input("Kérek egy számot: "))
        mennyiseg +=1
        osszeg += szam

    atlag: float = osszeg / mennyiseg
    return atlag