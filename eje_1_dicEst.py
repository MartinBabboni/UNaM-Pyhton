estudiantes ={}
menu = True
while menu:
    menu = input('\nSistema de carga de nota\n\nMenu\n\n1 - Carga de estudiante\n2 - Mostrar la cantidad de estudiantes cargados\n3 - Mostrar el promedio de cada estudiante\n4 - Mostrar promedio mas alto\nS - Salir\n')
    if menu =='1':
        nombre=input('Ingresá el nombre completo del estudiante => ').upper()
        if nombre in estudiantes:
            print('Ya se cargaron las notas de ', nombre)
        else:
            nota1= float(input(f'Ingresá la primer nota de {nombre} => '))
            nota2= float(input(f'Ingresá la segunda nota de {nombre} => '))
            estudiantes.setdefault(nombre, [nota1, nota2])
            print('\nSe cargaron las notas de ', nombre)
    elif menu =='2':
        if len(estudiantes)>0:
            print('Se han cargado las notas de ', len(estudiantes) ,' estudiantes, que son los siguientes: ')
            for estudiante in estudiantes:
                print(estudiante)
        else:
            print('Aún no se han cargado las notas de ningún estudiante')
    elif menu =='3':
        if len(estudiantes)>0:
            print('Los notas promedio de los estudiantes son las siguientes')
            for estudiante, notas in estudiantes.items():
                print(estudiante,' Promedio: ', (notas[0]+notas[1])/2)
        else:
            print('Aún no se han cargado las notas de ningún estudiante')
    elif menu =='4':
        if len(estudiantes)>1:
            print('El estudiante con el promedio más alto es: ')
            mejorpromedio = 0
            mejorEstudiante = []
            for estudiante, notas in estudiantes.items():
                if ((notas[0]+notas[1])/2)>mejorpromedio:
                    mejorpromedio = (notas[0]+notas[1])/2
                    mejorEstudiante = [estudiante, (notas[0]+notas[1])/2]
            print(mejorEstudiante[0],' tuvo un promedio de: ', mejorEstudiante[1])
        else:
            print('No se han cargado suficientes estudiantes para hacer una comparación')
    elif menu.upper() =='S':
        print('Hasta pronto\nGracias por utilizar ACNE-Software')
        menu=False
    else:
        print('La opción elegida no es válida')

