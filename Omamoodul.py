from random import*
import string
def salasona(k: int):
    sala="" 
    for i in range(k):
        t=choice(string.ascii_letters) 
        num=choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        saladus+=choice(t_num)
        return saladus


def registreerimine(u:list,p:list):
    nimi=input("sisesta oma nimi:")
    v=int(input("1-ese koostan parooli/n2-arvuti genireerib/n"))
    if v==1:
         pass 
    else:
         salasona=salasona(5)
         u.append(nimi)
         p.append(salasona)
    return u,p 



def autoriseerimine(u:list,p:list):
    nimi=input("sisesta oma nimi:")
    salasona=input("sisesta oma salasõna:")
    if nimi in u:
        ind=u.index(nimi)
        if salasona==p[ind]:
            print("tere tulemast!")
        else:
            print("vale salasõna!")
    else:
        print("nimi ei ole nimekirjas!")
