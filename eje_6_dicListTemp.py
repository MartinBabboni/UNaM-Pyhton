#! python3

'''
DICCIONARIO CON LISTAS Realice un programa para el almacenamiento de las
temperaturas de los 5 días laborales de la semana para su posterior procesamiento.
Para ello se debe presentar el siguiente menú:
1) Cargar temperaturas de un día.
2) Listar los días con temperaturas mayor al promedio.
f) Finalizar.
El programa SOLO finaliza si se ingresa la opción "f". En caso de ingresar
una opción distinta a las mostradas, se debe indicar por pantalla 
"OPCIÓN INCORRECTA" y pedir el reingreso.
Si se selecciona la opción 1, el usuario debe indicar el día que se quiere cargar
y SOLO se puede cargar si no fue cargado con anterioridad. Por cada día se
cargarán 3 temperaturas, las cuales deben pertenecer al intervalo [-25, 50], 
en caso de ingresar un valor fuera del rango pedir reingreso.
Si se selecciona la opción 2, se listan los días en los que la temperatura
fue superior al promedio para ello se debe verificar previamente que el 
diccionario no se encuentre vacío.
Cualquier ingreso no válido se debe indicar con un cartel por pantalla y solicitar el reingreso.
'''
dic = {'LUNES':[],'MARTES':[],'MIERCOLES':[],'JUEVES':[],'VIERNES':[]}
menu =''
while menu !='f':
    menu = input('Menú\n1 - Cargar las temperaturas del día\n2 - Listar los días con temperaturas mayores al promedio\nf - Salir\n=> ').lower()

    # 1 Ingreso de las temperaturas
    if menu == '1':
        dia = input('Ingrese el día de la semana que quiere cargar\n=> ').upper()
        if dia in dic:
            if len(dic[dia]) == 0:
                check1 = True
                while check1:
                    tempMin = float(input(f'Ingrese la temperatura mínima del día {dia}: '))
                    if tempMin >= -25 and tempMin <= 50:
                        dic[dia].append(tempMin)
                        check1 = False
                    else:
                        print('La temperatura debe estar en el rango de -25° a 50°')
                check2 = True
                while check2:
                    tempMed = float(input(f'Ingrese la temperatura a las 12:00 AM del día {dia}: '))
                    if tempMed >= -25 and tempMed <= 50:
                        dic[dia].append(tempMed)
                        check2 = False
                    else:
                        print('La temperatura debe estar en el rango de -25° a 50°')
                check3 = True
                while check3:
                    tempMax = float(input(f'Ingrese la temperatura máxima del día {dia}: '))
                    if tempMax >= -25 and tempMax <= 50:
                        dic[dia].append(tempMax)
                        check3 = False
                    else:
                        print('La temperatura debe estar en el rango de -25° a 50°')
            
            # Si ya se cargaron las temperaturas
            else:
                print('Ya se cargaron las temperaturas para el día', dia)
        # Si se ingresó un día que no existe
        else:
            print('No se cargaran las temperaturas para el dia', dia)
    
    # 2 Ver los días cuyas temperaturas estuvieron sobre el promedio
    # verificar que esten cargadas las temperaturas para todos los días
    elif menu =='2':
        contador = 0
        for dia in dic.values():
            if len(dia) !=0:
                contador +=1
        if contador == 5:
            sumatemp = 0
            for i in dic.values():
                sumatemp += i[0]+i[1]+i[2]
            promedio = sumatemp/15
            diasSobPro = []
            for j, t in dic.items():
                if (t[0]+t[1]+t[2])/3 > promedio:
                    diasSobPro.append(j)
            print('Los siguientes días registraron una temperatura media por sobre el promedio: ')
            for item in diasSobPro:
                print(item)
        else:
            print('Aún no se registraron las temperaturas de todos los días de la semana')
    # salida
    elif menu =='f':
        print('Gracias por usar ACNÉ Software Solution')

    # opcion incorrecta
    else:
        print('La opción elegida no está en el menú')

