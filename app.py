from utilidades import *


trabajador = []

while True:
    print("\nMenu:")
    print("1) Asignar sueldos aleatorios")
    print("2) calificar sueldo")
    print("3) ver estadisticas")
    print("4) reporte de sueldos")
    print("5) Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        calcular_trabajador(trabajador)
    elif opcion == '2':
        calificar_sueldos(trabajador)
    elif opcion == '3':
        ver_estadisticas(trabajador)
    elif opcion == "3":
        (trabajador)   
    elif opcion =="4":
        reporte_de_sueldos(trabajador)
    elif opcion == '5':
        guardar_trabajador_csv(trabajador)    
        break
    else:
        print("incorrecto ingrese un numero del 1 al 5.")
