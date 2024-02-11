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

# data=[10, 11, 15, 20, 30, 10]
# for value in data:
#     print("*" * value)
    
#4

# postiindeks=input("vvedi postiindeks: ")
# if len(postiindeks) != 5 or not postiindeks.isdigit():
#     print("nepravilno! vvedi 5 4isel")
# else:
#     cifra=int(postiindeks[0])
#     if cifra==1:
#         print("Tallinn")
#     elif cifra==2:
#         print("Narva, Narva-Jõesuu")
#     elif cifra==3:
#         print("Kohtla-Järve")
#     elif cifra==4:
#         print("Ida-Virumaa, Lääne-Virumaa, Jõgevamaa")
#     elif cifra==5:
#         print("Tartu linn")
#     elif cifra==6:
#         print("Tartumaa, Põlvamaa, Võrumaa, Valgamaa")
#     elif cifra==7:
#         print("Viljandimaa, Järvamaa, Harjumaa, Raplamaa")
#     elif cifra==8:
#         print("Pärnumaa")
#     elif cifra==9:
#         print("Läänemaa, Hiiumaa, Saaremaa")
#     else:
#         print("ne najdeno")
# if postiindeks[0] in ['1', '2', '3']:
#     print("ostavajtes doma!")
# else:
#     print("nosite maski!")

#5

n = int(input("skolko elementov"))
if n<2:
    print("nu hotjabq 2")
else:
    numbrid=[]
    for i in range(n):
        num=int(input(f"vvedi {i+1} element "))
        numbrid.append(num)
    print("iznachalno", numbrid)
    k=int(input("skolko hotite pomenatj??"))
    if k>n:
        print("a skolko net")
    else:
        for i in range(k//2):
            numbrid[i], numbrid[n-i-1] = numbrid[n-i-1], numbrid[i]
        print("teperj", numbrid)