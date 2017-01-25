#Liður 1
#biður um tölur
tala1 = float(input("Sláðu inn tölu: "))
tala2 = float(input("Sláðu inn tölu: "))
#prentar út tala1 * tala2
print(tala1, "*", tala2, "=", str(tala1 * tala2))

#Liður 2
#biður um fornafn og eftirnafn
fornafn = input("Sláðu inn fornafn: ")
eftirnafn = input("Sláðu inn eftirnafn: ")
#prentar út fornafn og eftirnafn
print("Halló", fornafn, eftirnafn)

#Liður 3
#biður um texta
texti = input("Sláðu inn texta: ")
#býr til teljara sem halda utan um hástafi og lágstafi
teljariHastafir = 0
teljariLagstafir = 0
teljariEftirHastaf = 0
#boolean sem er true ef síðasti stafur var hástafur
sidasthar = False
#for loop sem loopar eins oft og lengd textans
for i in range(len(texti)):
    #athugar hvort i-undi bókstafur í textanum sé hástafur
    if texti[i].isupper():
        #bætir 1 við teljara
        teljariHastafir += 1
        #gerir sidasthar að True
        sidasthar = True
    #athugar hvort i-undi bókstafur í textanum sé lágstafur og síðasti var hástafur
    elif texti[i].islower() and sidasthar == True:
        #bætir 1 við teljariEftirHastaf
        teljariEftirHastaf += 1
        #gerir sidasthar að False
        sidasthar = False
    #athugar hvort i-undi bókstafur í texta sé lágstafur
    if texti[i].islower():
        #bætir 1 við teljarann
        teljariLagstafir += 1
        #gerir sidasthar að False
        sidasthar = False
#prentar út niðurstöður
print("í þessum texta eru", teljariHastafir, "hástafir,", teljariLagstafir, "lágstafir og", teljariEftirHastaf, "lágstafir koma strax á eftir hástaf.")
