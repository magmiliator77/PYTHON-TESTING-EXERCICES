#numero del comic que has comprado, dependiendo del numero estara en una saga o otra()

numeroComic = int(input("Introduce el número del comic quehas comprado"))

if numeroComic == 0:
    print("ERROR, no existe ningun codigo menor que 0")
elif numeroComic>=1 and numeroComic <= 154:
    print("Tu comic es de la saga clásica")
elif numeroComic>=155 and numeroComic <= 211:
    print("Tu comic es de la saga de Dragon Ball Z")
elif numeroComic>= 212 and numeroComic <=  316:
    print("Tu comic es de la saga de Dragon Ball Super")
else:
    print("Ese comic no existe")