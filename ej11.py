#Como te llamas, tu edad, si eres mayor de edad o no.

nombre = str(input('¿Cómo te llamas?'))

edad = float(input('¿Cuántos años tienes?'))

if edad>=18:
    print(f'Hola, {nombre}, puedes entrar en la discoteca')
else:
    print(f'Hola, {nombre}, no puedes entrar en la discoteca')