#�lesanne 11 Arvamism�ng
from math import *
from random import *


#11 �lesane
print("Arvuti m�istatab numbrit 1-10 ja sina �ritad seda �ra arvata.")
a=randint(1,10)
vastus=int(input("mis arv on m�istatanud arvutit?: "))
k=1
while vastus!=a:
    print("�ra sa ei arvanud �ra, proovi uuesti!: ")
    vastus=int(input("Sisesta vastus: "))
    k+=1
    if k>2: 
        print("P��dlused on l�ppenud")      
        break
while True: 
     print("Palju �nne, sa arvasid �ra!",k )
     break
print()


#M�tle ise v�lja �lesanne, mis on vaja lahendada while tingimusega/while True/for kasutades. Lahenda nii while kui ka for abil.
while True:
    a=input("Kas sa tahad endale uue arvuti osta?: ")
    if a.upper()=="J�H" or a.upper()=="EI": break
if a.upper()=="J�H":
    while True:
        c=input("Kas tahad m�nguarvutit v�i tavalist?: ")
        if c.upper()=="M�NGUARVUTIT" or c.upper()=="TAVALIST": break
    if c.upper()=="M�NGUARVUTIT":
        while True:
            try:
                a1=float(input("Kui palju maksab korpus, mida soovite osta?: "))
                a2=float(input("Kui palju maksab protsessor, mida soovite osta?: "))
                a3=float(input("Kui palju maksab videokaart, mida soovite osta?: "))
                a4=float(input("Kui plaju maksab emaplaat, mida soovite osta?: "))
                a5=float(input("Kui plaju maksabm�lu mida soovite osta?: "))
                break
            except TypeError:
                print()
        hind5=a1+a2+a3+a4+a5 
        print(f"Teie arvuti maksab: {hind5}")
    else:
        print("Me m��me ainult m�nguarvuteid")
else:
    print("nagemist")
print()
