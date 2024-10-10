#calculo sin iva has comprado (precio) de los cuales (IVA%) son iva

producto = input('¿Que has comprado?')
precio = float(input('¿Cuanto te ha costado?'))
iva = int(input('¿Que porcentaje de IVA te han aplicado?'))

print(f'Has comprado {producto}, te ha costado {precio}€, de los cuales {precio*iva/100}% son IVA')

#CALCULO DE IVA
preciosinIVA = precio*(iva/100)



