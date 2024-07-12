import csv
import random


def agregar_producto(productos):
    trabajador = input("Ingrese el nombre del trabajador: ")
    calificar_sueldo = input("Ingrese la descripción del producto: ")
    sueldo = round(random.uniform(300000, 2500000), )  
    total = {'nombre': trabajador, 'descripcion': calificar_sueldo, 'precio': sueldo}
    trabajador.append(total)
    print(f"Producto {trabajador} agregado con precio {sueldo}.")


def calcular_trabajador():
    suma = sum(producto['precio'] for producto in calcular_trabajador)
    print(f"La suma de los precios de los productos es: {suma}")


def calificar_sueldos(productos):
    if productos:
        promedio = sum(producto['precio'] for producto in productos) / len(productos)
        print(f"El promedio de los precios de los productos es: {promedio}")
    else:
        print("No hay productos para calcular el promedio.")

def ver_estadisticas(productos):


def reporte_de_sueldos(prodcuto):
    

def salir_todo(producto):