#Caja registradora

productos={'franela':5,
            'pantalon':12,
            'calcetines':2,
            'sombrero':15,
            'mameluco':16}
inventario={'franela':3,
            'pantalon':1,
            'calcetines':10,
            'sombrero':2,
            'mameluco':4}
print ('Buenos días o tal vez buenas noches: ')
print ('''Menu principal:
        lista de precios = 0
        facturar= 1''')
chequear =input('escriba aqui su opcion basado en la clave expresada:')

if chequear =='lista de precios' or chequear == '0':
    
    print ('lista de precios: ',productos)
    a=input('si le satisface y desea continuar, type <<ok gracias>> : ')
    if a== 'ok gracias':
        chequear = 'facturar'
    else:
        print ('Igual procedamos a facturar por el bien del negocio')
        chequear = 'facturar'

if chequear == 'facturar' or chequear == '1':
    print('escriba el nombre de producto a facturar')
    total=0
    while chequear == 'facturar' or chequear == '1':
        item= input ('introduzca nombre del producto: ')
        #print (productos[item])
        if item != 'franela' and item != 'mameluco' and item != 'sombrero' and item != 'pantalon' and item != 'calcetines':
            print('lo sentimos, el producto que ingreso no fue nombrado correctamente o no hay mas en inventario.')
            error_item=input('si desea consultar inventario, marque 2 (si no lo desea, marque cualquier caracter): ')
            if error_item=='2':
                print(inventario)
                agregar= input('desea agregar otro producto al carrito? si/no: ')
                if agregar == 'no':
                    print('el monto a cancelar sera: $',total)
                    break
            if error_item != '2':
                agregar= input('desea agregar otro producto al carrito? si/no: ')
            elif agregar == 'no':
                
                print('el monto a cancelar sera: $',total)
                break
            else:
                agregar= input('desea agregar otro producto al carrito? si/no: ')
            if agregar == 'no':
                print('el monto a cancelar sera: $',total)
                break
        else:    
            total+= (productos[item])
            inventario[item] -= 1
            if inventario[item]== 0:
                print('te estas llevando the last ', item, 'disponible!')
                #productos.pop(item) #borrar franela del inventario
                print('total acumulado: $',total)
                agregar= input('desea agregar otro producto al carrito? si/no: ')
                if agregar == 'no':
                    print('el monto a cancelar sera: $',total)
                    break
            elif inventario[item]<0:
                print('fusible informatico') # si falla es aqui
                print (' lo sentimos, no hay mas ',item, '(s) disponibles')
                # fusible parte 2
                agregar= input('desea agregar otro producto al carrito? si/no: ')
                if agregar == 'no':
                    print('el monto a cancelar sera: $',total)
                    break
            else:

                print('restan ', inventario[item], item,'(s) disponibles')
                print('total acumulado: $',total)
                agregar= input('desea agregar otro producto al carrito? si/no: ')
                if agregar == 'no':
                    print('el monto a cancelar sera: $',total)
                    break
                
else:
    print('por favor verifique su ortografia')

#Falta validar el chequear y garantizar el item