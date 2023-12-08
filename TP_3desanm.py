import modil
print("\n")
print("\tBonjou, bonswa tout moun,")
print("\tTP sila a, se TP dat 3 desanm lan.")
print("\tPwogram sa a pèmèt ou fè adisyon, soustraksyon, miltiplikasyon, divizyon,")#
print("\t   eksponansyèl, faktoryèl epi kare yon nonb.") 
print("\tNan meni pi ba a, jis chwazi nimewo ki fè w plezi a.\n")
print("\t#--------/-MENI-/--------#")
print("\t| [1] Adisyon            |")
print("\t| [2] Soustrakyon        |")
print("\t| [3] Miltiplikasyon     |")
print("\t| [4] Divizyon           |")
print("\t| [5] Eksponansyèl       |")
print("\t| [6] Faktoryèl          |") 
print("\t| [7] Rasin kare         |")
print("\t#________________________#\n")
choice = int(input("\t- Ki nimewo ki koresponn ak operasyon ou swete fè a: "))
while(choice < 1 or choice > 7):
    choice = int(input("\t- Chwazi yon nonb ki nan entèval [1, 7]: "))
if (choice == 1):
    nb1 = int(input("\t- Endike premye nonb lan: "))
    nb2 = int(input("\t- Endike dezyèm nonb lan: "))
    result = modil.add(nb1, nb2)
    print("\tAdisyon: (" + str(nb1) + " + " + str(nb2) + ") = " + str(result))
elif (choice == 2):
    nb1 = int(input("\t- Endike premye nonb lan: "))
    nb2 = int(input("\t- Endike dezyèm nonb lan: "))
    result = modil.substract(nb1, nb2)
    print("\tSoustraksyon: (" + str(nb1) + " - " + str(nb2) + ") = " + str(result))
elif (choice == 3):
    nb1 = int(input("\t- Endike premye nonb lan: "))
    nb2 = int(input("\t- Endike dezyèm nonb lan: "))
    result = modil.multiply(nb1, nb2)
    print("\tMiltiplikasyon: (" + str(nb1) + " * " + str(nb2) + ") = " + str(result))
elif (choice == 4):
    nb1 = int(input("\t- Endike nonb ki se dividann lan: "))
    nb2 = int(input("\t- Endike nonb ki se divizè a: "))
    while(nb2 == 0):
        print("\tOu paka divize yon nonb pa '0'")
        nb2 = int(input("\t- Endike yon lòt divizè: "))
    result = modil.divide(nb1, nb2)
    print("\tDivizyon: (" + str(nb1) + " / " + str(nb2) + ") = " + str(result))
elif (choice == 5):
    nb1 = int(input("\t- Endike nonb ki se baz la: "))
    nb2 = int(input("\t- Endike nonb ki se pwisans lan: "))
    result = modil.exponent(nb1, nb2)
    print("\tRezilta (" + str(nb1) + "^" + str(nb2) + ") se " + str(result))
elif (choice == 6):
    nb1 = int(input("\t- Endike nonb lan: "))
    while(nb1 < 0):
        print("\tOu paka kalkile faktoryèl yon nonb negatif")
        nb1 = int(input("\t- Endike yon lòt nonb: "))
    result = modil.factorial(nb1)
    print("\tRezilta (" + str(nb1) + "!" + ") se " + str(result))
else:
    nb1 = int(input("\t- Endike nonb lan: "))
    while(nb1 < 0):
        print("\tRrasin kare yon nonb negatif enposib nan R")
        nb1 = int(input("\t- Endike yon lòt nonb: "))
    result = modil.square(nb1)
    print("\tRezilta (Radikal " + str(nb1) + ") se " + str(result))

print("\n\tMèsi dèske ou te itilize pwogram sila a.")
print("\t__GEORGES Jonathan___\n")