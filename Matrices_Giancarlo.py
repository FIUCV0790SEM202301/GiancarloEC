n = int(input('ingrese número de columnas: '))
m = int(input('ingrese número de filas: '))

matriz = [[0 for i in range(n)] for i in range(m)] # para que n y m sean iterables #se crea "lista de listas"

lista_vacia= []

for numero in range(m):
    lista_auxiliar = []
    print(lista_auxiliar) # se crean m filas
    for numero2 in range(n):
        lista_auxiliar.append(0) # para agregar n columnas
        
    lista_vacia.append(lista_auxiliar) # se configura la matriz en 0

print ('esqueleto:',lista_vacia)
llenado = 1
for fila in matriz:
    if (matriz.index(fila)) % 2 != 0: # para las filas impares, llenar al reves
        for columna in range(len(fila)):
            fila[-(columna+ 1)] = llenado
            llenado += 1
    else:
        for columna in range(len(fila)): # llenado comun
            fila[columna] = llenado
            llenado += 1


for m in matriz: # para dar estructura de matriz, se imprime fila por fila
    print(m)

