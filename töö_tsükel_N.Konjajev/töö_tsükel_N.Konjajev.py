#Ülesanne 11 Arvamismäng
from math import *
from random import *


#11 ülesane
print("Arvuti mõistatab numbrit 1-10 ja sina üritad seda ära arvata.")
a=randint(1,10)
vastus=int(input("mis arv on mõistatanud arvutit?: "))
k=1
while vastus!=a:
    print("Ära sa ei arvanud ära, proovi uuesti!: ")
    vastus=int(input("Sisesta vastus: "))
    k+=1
    if k>2: 
        print("Püüdlused on lõppenud")      
        break
while True: 
     print("Palju õnne, sa arvasid ära!",k )
     break
print()


#Mõtle ise välja ülesanne, mis on vaja lahendada while tingimusega/while True/for kasutades. Lahenda nii while kui ka for abil.
while True:
    a=input("Kas sa tahad endale uue arvuti osta?: ")
    if a.upper()=="JÄH" or a.upper()=="EI": break
if a.upper()=="JÄH":
    while True:
        c=input("Kas tahad mänguarvutit või tavalist?: ")
        if c.upper()=="MÄNGUARVUTIT" or c.upper()=="TAVALIST": break
    if c.upper()=="MÄNGUARVUTIT":
        while True:
            try:
                a1=float(input("Kui palju maksab korpus, mida soovite osta?: "))
                a2=float(input("Kui palju maksab protsessor, mida soovite osta?: "))
                a3=float(input("Kui palju maksab videokaart, mida soovite osta?: "))
                a4=float(input("Kui plaju maksab emaplaat, mida soovite osta?: "))
                a5=float(input("Kui plaju maksabmälu mida soovite osta?: "))
                break
            except TypeError:
                print()
        hind5=a1+a2+a3+a4+a5 
        print(f"Teie arvuti maksab: {hind5}")
    else:
        print("Me müüme ainult mänguarvuteid")
else:
    print("nagemist")
print()
