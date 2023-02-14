from random import*
from Omamoodul import*
u=[] 
p=[]
while True:
    v=input("1-registreerimine/n2-autoriseerimine/n3-välja")
    if v==1:
         u,p=registreerimine(u,p)
    elif v==2:
        autoriseerimine()
    elif v==3:
         break
    else:print("tee õige valik")