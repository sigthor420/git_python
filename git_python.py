#Liður 1
tala1 = float(input("Sláðu inn tölu: "))
tala2 = float(input("Sláðu inn tölu: "))

print(tala1, "*", tala2, "=", str(tala1 * tala2))

#Liður 2

fornafn = input("Sláðu inn fornafn: ")
eftirnafn = input("Sláðu inn eftirnafn: ")
print("Halló", fornafn, eftirnafn)

#Liður 3

texti = input("Sláðu inn texta: ")
teljariHastafir = 0
teljariLagstafir = 0
teljariEftirHastaf = 0
sidasthar = False

for i in range(len(texti)):
    if texti[i].isupper() and texti[i]:
        teljariHastafir += 1
        sidasthar = True
    elif texti[i].islower() and sidasthar == True:
        teljariEftirHastaf += 1
        sidasthar = False
    if texti[i].islower():
        teljariLagstafir += 1
        sidasthar = False

print("í þessum texta eru", teljariHastafir, "hástafir,", teljariLagstafir, "lágstafir og", teljariEftirHastaf, "lágstafir koma strax á eftir hástaf.")
