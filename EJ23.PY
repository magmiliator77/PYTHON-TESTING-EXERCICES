#guardanmos un numero en una variable y le preguntamos al usuario entre 1-10 y le decimos si has acertado o no, si no ha acertado puede
#reiniciar
#cotador de cuanstes veces lo has intentado


from random import *

numeroCorrecto = randint(1, 10)

contador = 0

reiniciar = 's'

while reiniciar != 'n':
    numeroIntroducido = int(input("Introduce un numero entre 1-10"))

    contador=contador+1

    if numeroIntroducido != numeroCorrecto:
        print("Has fallado")
        print (f'Llevas {contador} intentos')
        
        
    else:
        print("Has acertado :D")
        

    reiniciar = str(input("¿Quieres reiniciar (s/n)?"))

   