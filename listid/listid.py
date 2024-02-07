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

nimed=[]
for i in range (5):
    nimi=input("vvedi imja ")
    nimed.append(nimi)

print("sisestatud:", nimed)
nimed.sort()
print("sorteeritud:", nimed)
print("viimasena oli lisatud: ",nimi)
nimi=input("mis nimi on vaja asendada? ")
# indeks=nimed.index(nimi)
uus_nimi=input("uus nimi: ")
# nimed[indeks]=uus_nimi
nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
nimed=set(nimed) #ubiraet dublikatq
print(nimed)
vanused=[]
for i in range (5):
    v=int(input("vvedi vanus "))
    vanused.append(v)
summ=sum(vanused)
min_=min(vanused)
maxx=max(vanused)
kesk=summ/len(vanused)
print("keskmine {kesk}, \nSuurim on {maxx}, \nVaiksem on {min_}, \nSumma on {summ}")