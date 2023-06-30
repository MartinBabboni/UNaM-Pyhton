# 2
dicProductos = {}
ventasDia =[]
menu = ''
print(" - Bienvenidos Stock-Control - ")
while menu !='F':
    menu = (input("\nMenu\n1 - Carga de productos\n2 - Cargar la venta de un producto\n3 - Controlar el stock de productos\n4 - Ver resumen de ventas\n5 - Dar de baja un producto\nF - Finalizar el programa\n=> ")).upper()

    # 1 Carga de los productos
    if menu =='1':
        nomProd = input('Ingrese el nombre del producto => ').upper()

        if nomProd in dicProductos: # si el producto está en stock te tira estos datos
            print(f"El producto: {nomProd} ya está cargado en stock con los siguientes valores")
            print('Peso unitario: ',dicProductos[nomProd][0])
            print('Cantidad: ',dicProductos[nomProd][1])
            print('Precio: ',dicProductos[nomProd][2])
            print('Se registrará el nuevo peso y precio, y se sumaran las cantidades')
            nuevo =' nuevo' # variable para incorporar en el prompt de carga
            recupCantidad = dicProductos[nomProd][1] # variable para conservar el stock

        else: # si el producto no está en stock
            nuevo ='' # variable vacia para el prompt de carga
            recupCantidad = 0 # variable el stock valor de stock para un producto nuevo

        dicProductos[nomProd] = [0,0,0] # para que funcione el while se pone a cero todos los valores
        while dicProductos[nomProd][0]<=0:
            pesoProd = float(input(f'Ingrese el{nuevo} peso unitario del producto: {nomProd}\n(el valor debe ser positivo) => '))
            dicProductos[nomProd][0] = pesoProd
        while dicProductos[nomProd][1]<=0:
            cantProd = int(input(f'Ingrese la cantidad del producto: {nomProd} que se suma al stock\n(el valor debe ser positivo) => '))
            dicProductos[nomProd][1] = recupCantidad + cantProd
        while dicProductos[nomProd][2]<=0:
            precioProd = float(input(f'Ingrese el{nuevo} precio del producto: {nomProd} \n(el valor debe ser positivo) => '))
            dicProductos[nomProd][2] = precioProd

        print('\nSe cargo el producto ', nomProd,' con los siguientes parametros y valores:')
        print('Peso unitario: ', dicProductos[nomProd][0])
        print('Cantidad sumada al stock: ', dicProductos[nomProd][1])
        print('Precio: ', dicProductos[nomProd][2])

   # 2 Venta de los productos
    elif menu =='2':
        vendo ='1'
        while vendo=='1':
            prodVenta = input('Ingrese el nombre del producto a vender\n=> ').upper()
            if prodVenta not in dicProductos:
                print(f'El producto {prodVenta} no se encuentra en stock')
                vendo = input('Desea: \n1 - Cargar la venta de otro producto\nS - Salir al menú principal\n').upper()
            else:
                sigo ='1'
                while sigo =='1':
                    cantVenta = int(input('\nIngrese la cantidad de producto a vender\n=> '))
                    if cantVenta > dicProductos[prodVenta][1]:
                        print('No se cuenta con esa cantidad de producto.')
                        print('El stock disponible es de: ', dicProductos[prodVenta][1])
                        sigo = input('Desea: \n1 - Cargar otra cantidad\n2 - Vender otro producto\nS - Salir al menú principal\n').upper()
                        if sigo =='S':
                            vendo ='2'
                    else:
                        ventasDia.append([prodVenta, cantVenta*dicProductos[prodVenta][2]])
                        dicProductos[prodVenta][1] -= cantVenta
                        print('\nSe realizó una venta de ', prodVenta,' por un total de $',cantVenta*dicProductos[prodVenta][2])
                        sigo ='2'
                        vendo='2'

    # 3 Control de stock
    elif menu =='3':
        valorN = 0
        while valorN <=0:
            valorN = int(input('\nIngrese la cantidad de stock que considere crítica\n=> '))
        listaProd =[]
        for producto, valor in dicProductos.items():
            if valor[1] < valorN:
                listaProd.append([producto, valor[1]])
        if len(listaProd) > 0:
            print('\nLos siguientes productos tienen un stock critico')
            for i in range(len(listaProd)):
                print(f'El producto {listaProd[i][0]} tiene un stock de {listaProd[i][1]}')
        else:
            print('\nNo se encontraron productos con stock crítico')

    # 4 Resumen de ventas
    elif menu =='4':
        if len(ventasDia)>0:
            print('\nEn el transcurso del día se realizaron', len(ventasDia), 'ventas.')
            totalVentas = 0
            for i in range(len(ventasDia)):
                totalVentas += ventasDia[i][1]
            print('Por un monto total de ', totalVentas)
        else:
            print('\nAún no se realizó ninguna venta')

    # 5 Borrar un producto del diccionario
    elif menu =='5':
        borrar ='1'
        while borrar =='1':
            prod_a_borrar =input('Ingrese el nombre del producto a eliminar del stock\n=> ').upper()
            if prod_a_borrar in dicProductos:
                del dicProductos[prod_a_borrar]
                print('Se eliminó el producto', prod_a_borrar)
                borrar ='2'
            else:
                print('No existe el producto a eliminar')
                print('Los productos en stock son los siguientes:')
                for producto in dicProductos:
                    print(producto)
                borrar = input('\nDesea:\n1 - Eliminar otro producto\nS - Volver al menú principal\n=> ')

    # salir del programa
    elif menu=='F':
        print('\nQue tengas un buen día')

    # Opción incorrecta
    else:
        print('\nLa opción elegida no está en el menú')


