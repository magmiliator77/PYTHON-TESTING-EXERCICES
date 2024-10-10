#nombre, edad, sexo, mayor de edad hombre has ganado un premio, si no eres mayor de edad y no eres mujer no has ganado nada

nombre = (input('¿Cómo te llamas?'))

edad = float(input('¿Cuántos años tienes?'))

sexo = (input('¿Eres hombre o mujer?'))

if edad>=18 and sexo==('H'):
    print(f'hola, {nombre} has ganado un premio')
else:
    print(f'No has ganado nada')