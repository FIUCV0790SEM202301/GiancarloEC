#Parcial2. Gestor de Cuentas Bancarias
#Desarrollar un programa para la gestion de cuentas Bancarias
#El programa debe manejar transacciones como depositos, retiros y consulta de saldos. 
#info y transacciones almacenados y recuperados en Json
import json
def read_json():
    with open("txt.json") as file:
        data = json.load(file)
        return (data)
def write_json(data):
    with open("txt.json", "w") as file:
        json.dump(data, file)

def abrirCuenta(registro): ## por probar
    nombre = input('Introduzca el nombre del beneficiario: ')
    numero_de_cuenta = "" ####################################debe ser unico
    saldo=""
    while True: #para validar que sea numerico
        numero_de_cuenta = input('Introduzca la numero de cuenta unico del beneficiario: ')
        if numero_de_cuenta.isnumeric():
            for nc in registro.values():
                if numero_de_cuenta == nc:
                    print('El numero de cuenta ya se encuentra asignado a otro beneficiario')
                else:
                    #registro[nombre]=["numero de cuenta"]
                    break
                            
        else:
            print('Verifique el numero de cuenta por favor, garantice que no tenga caracteres de tipo string: ')
        saldo = input('Introduzca saldo del beneficiario: ')
        if saldo.isnumeric():
            break
        else:
            print('Verifique que no hayan str en el campo de <<saldo>> por favor: ')
    registro[nombre] = {"numero de cuenta": (numero_de_cuenta), "saldo":float(saldo) }
    


def mostrarBeneficiarios(registro): ##por probar
    for beneficiario in registro.keys():
        print("Nombre: ",beneficiario, "\nNumero de cuenta: ",registro[beneficiario]["numero de cuenta"], "\nsaldo: ", registro[beneficiario]["saldo"]) 

def consultarSaldo(registro): ## por probar
    
    while True:
        nro_cuenta= input('Ingrese el numero de cuenta para verificar saldo disponible: ')
        if nro_cuenta.isnumeric():
            break
        else:            
            print('Por favor verifique que el numero de cuenta no contenga caracteres del tipo string')
    
    for beneficiario in registro.keys():
        
            if nro_cuenta== registro[beneficiario]["numero de cuenta"]:
                print("saldo disponible es: ", registro[beneficiario]["saldo"])

                break

def retirarMonto (registro):
    
    while True:
        monto_a_retirar= input('Ingrese el monto que desea retirar: ')
        if monto_a_retirar.isnumeric():
            monto_a_retirar=float(monto_a_retirar)
            break
        else:
            print('Verifique que el monto este expresado solo en numeros: ')

    while True:
        nro_cuenta= input('Ingrese el numero de cuenta para retirar: ')
        if nro_cuenta.isnumeric():
            int(nro_cuenta)
            break
        else:            
            print('Por favor verifique que el numero de cuenta no contenga caracteres del tipo string')

    for beneficiario in registro.keys():
        if nro_cuenta==registro[beneficiario]["numero de cuenta"]:
            saldo_disp= registro[beneficiario]["saldo"]
            if float(saldo_disp) >= float(monto_a_retirar):
                registro[beneficiario]["saldo"]-= monto_a_retirar
                print('Exito, el saldo restante es: ', registro[beneficiario]["saldo"])
            else:
                print('Lo sentimos, su saldo es insuficiente para realizar esta transaccion')

def depositarMonto (registro):
    while True:
        monto_a_depositar= input('Ingrese el monto que desea depositar: ')
        if monto_a_depositar.isnumeric():
            monto_a_depositar=float(monto_a_depositar)
            break
        else:
            print('Verifique que el monto este expresado solo en numeros: ')

    while True:
        nro_cuenta= input('Ingrese el numero de cuenta para depositar: ')
        if nro_cuenta.isnumeric():
            int(nro_cuenta)
            break
        else:            
            print('Por favor verifique que el numero de cuenta no contenga caracteres del tipo string')

    for beneficiario in registro.keys():
        if nro_cuenta==registro[beneficiario]["numero de cuenta"]:
            saldo_disp= registro[beneficiario]["saldo"]
            
            registro[beneficiario]["saldo"]+= monto_a_depositar
            print('Exito, el saldo restante es: ', registro[beneficiario]["saldo"])

def interactuar():
    data = read_json()
    while True:
        entrada_ppal = input("\n\nIngrese la clave que corresponda a la accion que desea ejecutar :\n1)Agregar Beneficiario\n2)Listar Beneficiarios\n3)Consultar Saldo\n4)Retirar monto\n5)Depositar monto\n6)Guardar Datos\n7)Salir\n\nIngrese la clave correspondiente: ")

        entrada_valida = False

        while not entrada_valida== True: #para que se repita hasta que sea cierto
            if entrada_ppal in ["1", "2", "3", "4", "5", "6", "7"]:
                entrada_valida = True
                break
            else:
                print("\nEntrada invalida. Verifique e intente de nuevo\n")
                ok=input('<<ok>> para continuar: ')
            if ok=='ok':
            
                entrada_ppal = input("\n\nIngrese la clave que corresponda a la accion que desea ejecutar :\n1)Agregar Beneficiario\n2)Listar Beneficiarios\n3)Consultar Saldo\n4)Retirar monto\n5)Depositar monto\n6)Guardar Datos\n7)Salir\n\nIngrese la clave correspondiente: ")
        
        if entrada_ppal == "1":
            abrirCuenta(data)
        elif entrada_ppal == "2":
            if data=={}:
                print('No hay datos en el registro. Por favor abra al menos una cuenta e intente de nuevo')
                exit()
            mostrarBeneficiarios(data)
        elif entrada_ppal == "3":
            if data=={}:
                print('No hay datos en el registro. Por favor abra al menos una cuenta e intente de nuevo')
                exit()
            consultarSaldo(data)
        elif entrada_ppal == "4":
            if data=={}:
                print('No hay datos en el registro. Por favor abra al menos una cuenta e intente de nuevo')
                exit()
            retirarMonto(data)
        elif entrada_ppal == "5":
            if data=={}:
                print('No hay datos en el registro. Por favor abra al menos una cuenta e intente de nuevo')
                exit()
            depositarMonto(data)
        elif entrada_ppal == "6":
            if data=={}:
                print('No hay datos en el registro. Por favor abra al menos una cuenta e intente de nuevo')
                exit()
            write_json(data)
        elif entrada_ppal== "7":
            exit()
interactuar()

    



   