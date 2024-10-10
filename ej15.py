#q coche tienes, marca y modelo juntas, matricula y el distintivo, en funcion del distintivo podra entrara a la zona de baja emisiones, si la posicoin es 0 o ECO puede pasar a la zona de baja emisiones

marcaModelo = str(input('¿Cuál es la marca y el modelo de tu coche?'))

matricula = int(input('¿Cuál es la matricula?'))

distintivo = input('Introduce el distintivo del coche(0/ECO/B/C)')

if distintivo == 'ECO' or  distintivo == '0':
    print(f'Puedes pasar a la zona de bajas emisiones')
else:
     print(f'No puedes pasar a la zona de baja emisiones')