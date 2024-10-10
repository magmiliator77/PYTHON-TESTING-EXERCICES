# nombre de el equipo, posicion en la tabla, si estas desde la cuarta hasta la 1 vas a campion si no no

nombreEquipo = str(input('¿Cuál es el nombre de tu equipo?'))

posicionTabla = float(input('¿Cúal es la posicion en la tabla?'))

if posicionTabla<=4:
    print(f'El equipo, {nombreEquipo}, esta en la champion')
else:
     print(f'El equipo, {nombreEquipo}, no estas en la champion')