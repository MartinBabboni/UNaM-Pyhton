#! python3
# eje_4_listDic.py - Debería hacer lo siguiente

'''
    LISTAS CON DICCIONARIOS - Se desea desarrollar un programa para el control de empleados en una empresa. Los empleados deben almacenar en una lista.

Debe mostrar en pantalla el siguiente menú:
MENU:

1: Carga de empleados

2: Cantidad de empleados por turno

3: Promedio de horas por sector

S: Salir

Si el usuario elige la opcion 1, debe preguntar cuántos empleados desea cargar (mayor a 0 y menor a 1000).
Por cada empleado se debe crear un diccionario con las siguientes claves y valores:
“legajo” : un número entero entre 0 y 1000
“edad” : un número entero entre 18 y 65
“sector” : un caracter (M: Mantenimiento, A: Administración, O: Operarios)
“turno” : un caracter (M o T)
“horas”: un número entre 10 y 40
Una vez cargado, el diccionario para un empleado se debe agregar a la lista de empleados
Si el usuario elige la opcion 2 , debe ingresar un turno elegido por el usuario y mostrar en pantalla la cantidad de empleados que trabajan en dicho turno.
Si el usuario elige la opcion 3 , debe ingresar un sector elegido por el usuario y el programa debe calcular y mostrar el promedio de horas de trabajo en el sector elegido.'''

empleados = []
menu = ''
print('Bienvenido al sistema de explotación laboral ACNE')
while menu != 'S':
    menu = input('\nMenú\n1 - Cargar empleados\n2 - Cantidad de empleados por turno\n3 - Promedio de horas por sector\nS - Salir\n=> ').upper()

    # 1 Carga de empleados
    if menu == '1':
        cantEmpleado = int(input('Ingrese la cantidad de empleados que desea cargar\=> '))
        if cantEmpleado > 0 and cantEmpleado < 1000:

            for empleado in range(len(empleados), len(empleados)+cantEmpleado): # Si hago dos cargas, debe comenzar por un indice mayor a los elementos que ya hay en la lista.
                empleados.append({'legajo':None, 'edad': None, 'sector': None, 'turno': None, 'horas': None})

                # cargar el nro de legajo, no deberia repetirse
                while empleados[empleado]['legajo'] == None:
                    print('\nVa a ingresar el empleado Nº', empleado+1)
                    legajo = int(input(f'Ingrese el número de legajo, debe estar comprendido entre 0 y 1000\n=> '))
                    if legajo >= 0 and legajo < 1000:
                        if len(empleados) == 1:
                            empleados[empleado]['legajo'] = legajo
                        else:
                            for dic in range(len(empleados)-1): # es len(empleado)-1 => si recorre toda la lista se compara con si mismo
                                if empleados[dic]['legajo'] == legajo:
                                    print('El número de legajo:', legajo, ' ya está registrado')
                                    empleados[empleado]['legajo'] = None
                                    break
                                else:
                                    empleados[empleado]['legajo'] = legajo
                    else:
                        print('El número de legajo debe estar comprendido entre 0 y 1000')

                # cargar edad
                while empleados[empleado]['edad'] == None:
                    edad = int(input('Ingrese la edad del empleado\n=> '))
                    if edad >= 18 and edad <= 65:
                        empleados[empleado]['edad'] = edad
                    else:
                        print('La edad debe estar comprendida entre 18 y 65 años')

                # cargar sector
                while empleados[empleado]['sector'] == None:
                    print('Ingrese el sector al cual pertenece el empleado\nM: Mantenimiento,\nA: Administración,\nO: Operarios')
                    sector = input('=>').upper()
                    if sector == 'M' or sector == 'A' or sector == 'O':
                        empleados[empleado]['sector'] = sector
                    else:
                        print('El sector elegido no corresponde a esta organización')

                # cargar turno
                while empleados[empleado]['turno'] == None:
                    turno = input('Ingrese el turno del empleado\nM - Mañana\nT - Tarde\n=> ').upper()
                    if turno == 'M' or turno == 'T':
                        empleados[empleado]['turno'] = turno
                    else:
                        print('El turno elegido no corresponde a esta organización')

                # cargar horas
                while empleados[empleado]['horas'] == None:
                    horas = int(input('Ingrese las horas semanales que realiza el empleado\n=> '))
                    if horas >= 10 and horas <= 40:
                        empleados[empleado]['horas'] = horas
                    else:
                        print('El empleado debe trabajar entre 10 y 40 horas')

                # fin de un empleado
                print('\nSe cargaron los datos correspondientes al legajo:',legajo)

            # fin de la carga de N empleados
            print('\nSe cargaron', cantEmpleado,'legajos')
        
    # 2 Consultar la cantidad de empleados por turno
    elif menu == '2':
        consultaT = input('Ingrese el turno del cual quiere conocer la cantidad de empleados\nM - Mañana\nT - Tarde\n=> ').upper()
        if consultaT =='M' or consultaT =='T':
            consultaTEmpl = 0
            for i in range(len(empleados)):
                if empleados[i]['turno'] == consultaT:
                    consultaTEmpl +=1
            if consultaTEmpl == 0:
                print('En el turno elegido no hay empleados')
            else:
                print('En el turno elegido trabajan ', consultaTEmpl, ' empleados.')
        else:
            print('El turno elegido no corresponde a esta organización')

    # 3 Consultar promedio de horas por sector
    elif menu == '3':
        print('Ingrese el sector del cual quiere conocer el promedio de horas trabajadas por empleado\nM: Mantenimiento,\nA: Administración,\nO: Operarios')
        consultaS = input('=>').upper()
        if consultaS == 'A' or consultaS == 'M' or consultaS == 'O':
            consultaSHoras = 0
            consultaSEmple = 0
            for i in range(len(empleados)):
                if empleados[i]['sector'] == consultaS:
                    consultaSEmple += 1
                    consultaSHoras += empleados[i]['horas']
            if consultaSEmple == 0:
                print('En el sector elegido no hay empleados')
            else:
                print('En el sector elegido se trabaja un promedio de',round(consultaSHoras/consultaSEmple, 2) ,' horas semanales.')
        else:
            print('El sector elegido no corresponde a esta organización')

    # 4 opción de menú incorrecta
    else:
        print('La opción elegida no está en el menú')

# Al salir del menú
print('Gracias por utilizar el sistema de administración laboral ACNE')









