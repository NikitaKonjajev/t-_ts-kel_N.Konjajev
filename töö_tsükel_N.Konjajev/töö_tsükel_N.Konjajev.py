#Ülesanne 11 Arvamismäng
from math import *
from random import *
#1
p=0
while True:
    number= int(input("Sisestage number suurem kui 10: "))
    p+=1
    if number >= 10:
        print("Õigest")
        break
    else:
        print("Arv on liiga väike",p)
print("katsed", p)
print

#22
print("Ma tah kommi")
katsed=0
while True:
    answer=input("Tahan kommi")
    katsed+=1
    if answer.lower()=="kommi":
        print(f"Teil kommid kirjutakse kulus {katsed} katse.")
        break
print

#22.1
katsed=0
answer=""
if answer.lower():
    while answer!="komm":
        answer=input("Taham kommi!")
        katsed+=1
    print(f"Katsed: {katsed}")

#11 ülesane
print("Arvuti mõistatab numbrit 1-10 ja sina üritad seda ära arvata.")
a=randint(1,10)
vastus=int(input("mis arv on mõistatanud arvutit?: "))
k=p=1
while vastus!=a:
    print("Ära sa ei arvanud ära, proovi uuesti!: ")
    vastus=int(input("Sisesta vastus: "))
    k+=1
    p+=1
    if k>2: 
        print("Püüdlused on lõppenud")      
        b=input("Kas proovi veel kord: ")
        if b.upper()=="JÄH":
            k=0
            continue
        else:
            break
if vastus==a:
     print("Palju õnne, sa arvasid ära!",p )
     
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
                break
            except: 
                print("TypeError")
        while True:
            try:
                a2=float(input("Kui palju maksab protsessor, mida soovite osta?: "))               
                break
            except: 
                print("TypeError")
        while True:
            try:
                a3=float(input("Kui palju maksab videokaart, mida soovite osta?: "))               
                break
            except: 
                print("TypeError")
        while True:
            try:
                a4=float(input("Kui plaju maksab emaplaat, mida soovite osta?: "))               
                break
            except: 
                print("TypeError")
        while True:
            try:
                a5=float(input("Kui plaju maksabmälu mida soovite osta?: "))               
                break
            except: 
                print("TypeError")
        hind5=a1+a2+a3+a4+a5 
        print(f"Teie arvuti maksab: {hind5}")
    else:
        print("Me müüme ainult mänguarvuteid")
else:
    print("nagemist")
print()



#1 ülessane 6
for x in range(5):
    print("*****")

#1 ggggg
for i in range(1, 11):
    print("*"*i, end="")
    print()

for i in range(1,5):
    x=str("*"*i).center(18," ")
    print(x, end="") 
    print()
for i in range(1,7):
    x=str("*"*(i+2)).center(18," ")
    print(x, end="") 
    print()