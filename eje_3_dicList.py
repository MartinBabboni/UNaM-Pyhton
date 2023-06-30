#! python3
# eje_3_dicList.py - Debe hacer lo siguiente

'''    DICCIONARIOS CON LISTAS - Escribir un programa que permita gestionar la base de datos de clientes de una empresa.

Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su DNI, y el valor será otro
diccionario con los datos del cliente (nombre, dirección, teléfono, correo, tipocliente), donde preferente tendrá
el valor True si se trata de un cliente preferente.

El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente,
(2) Eliminar cliente,
(3) Mostrar cliente,
(4) Listar todos los clientes,
(5) Listar clientes preferentes,
(6) Terminar.
En función de la opción elegida el programa tendrá que hacer lo siguiente:
    Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    Preguntar por el DNI del cliente y eliminar sus datos de la base de datos.
    Preguntar por el DNI del cliente y mostrar sus datos.
    Mostrar lista de todos los clientes de la base datos con su DNI y nombre.
    Mostrar la lista de clientes preferentes de la base de datos con su DNI y nombre.
    Terminar el programa.'''

dicCliente ={}
menu =''
print('Bienvenidos al GESTOR DE CLIENTES ANCE')
while menu !='6':
    menu =input('\nMenú principal\n1 - Añadir un cliente\n2 - Eliminar un cliente\n3 - Ver los datos de un cliente\n4 - Ver la lista de clientes\n5 - Ver la lista de clientes preferentes\n6 - Terminar\n=> ')

    # 1 Añadir clientes
    if menu =='1':
        cliente =int(input('Ingresá el DNI del nuevo cliente\n=> '))
        nombre = input(f'Ingresá el nombre y apellido del cliente: {cliente}\n=> ').upper()
        direccion = input(f'Ingresá la dirección de: {nombre}\n=> ').upper()
        telefono = input(f'Ingresá el teléfono de: {nombre}\n=> ')
        mail = input(f'Ingresá el mail de: {nombre}\n=> ')
        preferente = input(f'{nombre} ¿es cliente preferente?\n1 - Sí\n2 - No\n=> ')
        if preferente == '1':
            preferente = True
        else:
            preferente = False
        dicCliente[cliente] = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'mail': mail, 'tipocliente': preferente}
        print('Se cargaron los datos del cliente:', cliente)

    # 2 Eliminar cliente
    elif menu == '2':
        cliente = int(input('\nIngresá el DNI del cliente que querés eliminar de la base\n=> '))
        if cliente in dicCliente:
            del dicCliente[cliente]
            print('Se eliminó el cliente: ', cliente)
        else:
            print('El DNI ingresado no corresponde a un cliente.')

    # 3 Ver los datos de un cliente
    elif menu == '3':
        cliente = int(input('\nIngresá el DNI del cliente para ver sus datos\n=> '))
        if cliente in dicCliente:
            print('Datos del cliente:', cliente)
            print('Nombre:', dicCliente[cliente]['nombre'])
            print('Dirección: ',dicCliente[cliente]['direccion'])
            print('Teléfono: ', dicCliente[cliente]['telefono'])
            print('Mail: ', dicCliente[cliente]['mail'])
            if dicCliente[cliente]['tipocliente']:
                print('Cliente Preferente')
        else:
            print('El DNI ingresado no corresponde a un cliente')

    # 4 Ver la lista de clientes
    elif menu == '4':
        if len(dicCliente)>0:
            print('\n La siguiente es la lista de clientes:')
            for cliente in dicCliente:
                print('Cliente:', cliente,'Nombre:', dicCliente[cliente]['nombre'])
        else:
            print('\nAún no se han ingresado datos de clientes.')

    # 5 Ver la lista de clientes preferentes
    elif menu =='5':
        if len(dicCliente)>0:
            prefer = []
            for cliente in dicCliente:
                if dicCliente[cliente]['tipocliente']:
                    prefer.append([cliente, dicCliente[cliente]['nombre']])
            if len(prefer)>0:
                print('\nLos siguientes clientes tienen categoría Preferente: ')
                for i in range(len(prefer)):
                    print('Cliente:', prefer[i][0], 'Nombre: ', prefer[i][1])
            else:
                print('\nAún no hay clientes en la categoría Preferente')
        else:
            print('\nAún no se han ingresado datos de clientes.')

    # Salida
    elif menu =='6':
        print('Gracias por utilizar el GESTOR DE CLIENTES ANCE\nQue tengas un buen día')

    # Opcion incorrecta
    else:
        print('\nLa opción elegida no está en el menú')

