#1
# from string import punctuation
# vokaali=["a","u","i","o","e","ü","ä","õ","ö","y"]
# konsonanti="qwrtpsdfghjklzxcvbnm"
# märgid=punctuation
# tuhikud=[" "]
# v=k=m=t=0
# tekst=input("sisesta tekst")
# print(tekst)
# tekst_list=list(tekst)
# print(tekst_list)
# for element in tekst_list:
#     if element.lower() in vokaali:
#         v+=1
#     elif element.lower() in konsonanti:
#         k+=1
#     elif element in märgid:
#         m+=1
#     elif element in tuhikud:
#         t+=1
# print("vokaali :",v)
# print("konsonanti :",k)
# print("kirjavahemärgid: ",m)
# print("tuhikud: ", t)

#2

# nimed=[]
# for i in range (5):
#     nimi=input("vvedi imja ")
#     nimed.append(nimi)

# print("sisestatud:", nimed)
# nimed.sort()
# print("sorteeritud:", nimed)
# print("viimasena oli lisatud: ",nimi)
# nimi=input("mis nimi on vaja asendada? ")
# # indeks=nimed.index(nimi)
# uus_nimi=input("uus nimi: ")
# # nimed[indeks]=uus_nimi
# nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
# nimed=set(nimed) #ubiraet dublikatq
# print(nimed)
# vanused=[]
# for i in range (5):
#     v=int(input("vvedi vanus "))
#     vanused.append(v)
# summ=sum(vanused)
# min_=min(vanused)
# maxx=max(vanused)
# kesk=summ/len(vanused)
# print("keskmine {kesk}, \nSuurim on {maxx}, \nVaiksem on {min_}, \nSumma on {summ}")

#3

# from random import *
# from string import *
# while True:
#     try:
#         n=int(input("mitu rida loome?"))
#         break
#     except:
#         print("vale tuup")
# while True:
#     try:
#         S=input("mis sumbol")
#         if S in punctuation:
#             break
#         else:
#             print("vale tuup")
#     except:
#         print("vale tuup")
# for i in range(n):
#     print(randint(1, 25)*S)
    
    
#4

# indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
# while True:
#     indeks=input("indeks: ")
#     if len(indeks)==5 and indeks.isdigit() and indeks[0]!="0":
#         print("sa elad piirkonnas",indeksid[int(indeks[0])-1])
#         if indeks[0]=="1"or indeks[0]=="2" or indeks[0]=="3": #indeks[0] in ["1","2","3"]:
#             print("Оставайтесь дома!")
#         else:
#             print("Носите маски!")
#     else:
#         print("sisesta uus inkedks")
       

#5
# from random import *
# from string import *
# rida=[]
# n=randint(2,25)
# for i in range(n):
#     rida.append(choice(ascii_uppercase))
# print(rida)
# n=int(input("mitu paari vahetada"))
# if len(rida)//2>=n:
#     for i in range(n):
#         abi=rida[i]
#         rida[i]=rida[len(rida)-1-i]
#         rida[len(rida)-1-i]=abi
# else:
#     print("liiga vahe elemente")
# print(rida)

#6

# arvud=[1,2,3,4,5,6,122,44,5]
# print(arvud)
# max_=max(arvud)
# indeks=arvud.index(max_)
# max_=int(max_/len(arvud))
# arvud[indeks]=max_
# print(arvud)



#11

n=int(input("sisestage tähtede arv: "))
lowercase_alphabet=[chr(i) for i in range(97, 97 + n)]
more_lowercase_alphabet=[letter*(i + 1) for i, letter in enumerate(lowercase_alphabet)]
print("alaregistri järjend:",lowercase_alphabet)
print("rohkem järjend:",more_lowercase_alphabet)

#12

import random
numb=[random.randint(1, 100) for _ in range(10)]
print("enne:", numb)
min_value=min(numb)
max_value=max(numb)
min_index=numb.index(min_value)
max_index=numb.index(max_value)
numb[min_index],numb[max_index]=numb[max_index],numb[min_index]
print("parast:", numb)

#10

tootajad=[
    {"nimi": "Aadu Suur", "vanus": 56, "palk": 2500},
    {"nimi": "Malle Kapsas", "vanus": 42, "palk": 1500},
    {"nimi": "Uudo Koba", "vanus": 32, "palk": 700},
    {"nimi": "Tiit Kopikas", "vanus": 22, "palk": 550},
    {"nimi": "Vahur Vana", "vanus": 67, "palk": 870}
]
suurima_palgaga_tootaja=max(tootajad, key=lambda x: x["palk"])
print("kõige suurema palgaga töötaja:", suurima_palgaga_tootaja["nimi"])
print("palga suurus:", suurima_palgaga_tootaja["palk"])
keskmine_palk=sum(tootaja["palk"] for tootaja in tootajad)/len(tootajad)
print("keskmine palk:", keskmine_palk)
rohkem_keskmisest_teenijaid=sum(1 for tootaja in tootajad if tootaja["palk"] > keskmine_palk)
print("keskmisest palgast rohkem teenijaid:", rohkem_keskmisest_teenijaid)
keskmine_vanus=sum(tootaja["vanus"] for tootaja in tootajad) / len(tootajad)
print("keskmine vanus:", keskmine_vanus)
keskmisest_vahem_teenijad=[tootaja["vanus"] for tootaja in tootajad if tootaja["palk"] <= keskmine_palk]
keskmisest_rohkem_teenijad=[tootaja["vanus"] for tootaja in tootajad if tootaja["palk"] > keskmine_palk]
print("keskmised vanused neile, kes teenivad keskmisest vähem:", sum(keskmisest_vahem_teenijad) / len(keskmisest_vahem_teenijad))
print("keskmised vanused neile, kes teenivad keskmisest rohkem:", sum(keskmisest_rohkem_teenijad) / len(keskmisest_rohkem_teenijad))