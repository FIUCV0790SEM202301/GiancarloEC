#caracol2.0 suponiendo equinoccio
h= float(input('profundidad del pozo en metros: '))
ld=float(input('ascenso por dia del caracol en metros: ')) # ascenso tras 12 horas)
ln= float(input('descenso por noche del caracol en metros: ')) #descenso tras 12 horas
desplazamiento=0
dia=0
if ln > ld and ld<= h: #si el caracol sube exactamente la profundidad del pozo no saldra, solo quedara en el limite
    print ('el caracol no saldra del pozo nunca')
elif ld > h:
    print('el caracol sale al primer dia')

while desplazamiento <= h:
    desplazamiento+= ld
    if desplazamiento <= h:
        desplazamiento-= ln
    dia+=1
    if desplazamiento > h:
        print ('el caracol sale tras ', dia, 'dia(s)')