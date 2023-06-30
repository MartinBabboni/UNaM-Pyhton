#! python3
# dicListEst.py - Debe hacer lo siguiente
'''

    DICCIONARIOS CON LISTAS - Se desea almacenar los datos de 3 alumnos.

Definir un diccionario cuya clave sea el número de documento del alumno.

Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.Tener en cuenta que un alumno puede cursar varias materias. Debe ir agregandole materias mientras el usuario lo desee.

Crear las siguientes opciones del menu:

    Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
    Listado de todos los alumnos con sus notas
    Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
'''
 # modelo de dic => dic = {40123456: [('Matematica', 10),('Ingles', 9), ('Física', 10)], 41852987: [('Química', 9), ('Geografía', 10)] }
dic = {}
menu = ''
print('Bienvenido al sistema ACNE de gestión de notas')
while menu != 'S':
    menu = input('\nMenú\n1 - Cargar estudiantes\n2 - Listar estudiantes y sus notas\n3 - Consultar las notas de un estudiante en particular\nS - Salir\n=> ').upper()

    # 1 Carga de los estudiantes
    if menu = '1':
        dni = int(input('Ingrese el número de DNI del estudiante\n=> '))
        dic.setdefault(dni, [])
        materia = input('Ingrese la materia\n => ').upper()
        check = True
        for i in range(len(dic[dni])):
            if dic[dni][i][0] == materia:
                check = False
                print('Ya se cargó la nota de la materia: ', materia,' para es estudiante: ', dni)
                break
            else:
                check = True
        if check = True:
            nota = input('Ingrese la nota para', materia,'=> ')
            dic[dni]
