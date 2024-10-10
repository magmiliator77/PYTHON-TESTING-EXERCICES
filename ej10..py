#tu nombre y la nota de un asignatura, si ha sacado un 5 ha aprobado y si no np has aprobado

nombre = str(input('¿Cómo te llamas?'))

nota = float(input('Introduce tu nota de una asignatura'))

if nota >= 5:
    print(f'Hola {nombre}, has aprobado')

else:
    print(f'Hola {nombre}, has suspendido, lo siento')