## nombre de el equipo, posicion en la tabla, si estas desde la cuarta hasta la 1 vas a campion si no no

nombreEquipo = str(input('¿Cuál es el nombre de tu equipo?'))

posicionTabla = float(input('¿Cúal es la posicion en la tabla?'))

if posicionTabla<=4 and posicionTabla>0:
    print(f'el equipo, {nombreEquipo}, a la champion')
elif posicionTabla==5:
     print(f'el equipo, {nombreEquipo}, a la Eurocopa league')
elif posicionTabla==6:
      print(f'el equipo, {nombreEquipo}, a la Conference league')
elif posicionTabla>=7 and posicionTabla<=17: 
      print(f'el equipo, {nombreEquipo}, a la Permanencia')

elif posicionTabla>=18 and posicionTabla<=20:
      print(f'el equipo, {nombreEquipo}, al Descenso')

else:
      print(f'ERROR')