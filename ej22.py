#metemos todo es un bucle, preguntar al usuario desea introducir un numero

salir ='n'

while salir!='s':
    numero = int(input("Introduce un numero"))
    if numero % 2 ==0:
        print("Tu numero es par")
    else:
        print("Tu numero es impar")

    salir = input('¿Desea salir del prigrama (s/n)?')

    #IMPORTANTE, EJERCICIO DE EXAMEN!!!!!!!