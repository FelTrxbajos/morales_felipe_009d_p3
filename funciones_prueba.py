import os
import time
import msvcrt
import numpy

hotel = numpy.zeros(2,10)
lista_rut = []
lista_nombres = []
lista_id = []
nombre_mascota = []
lista_fila = []
lista_columna = []
id_unico = 1

def mostrar_menu ():
    os.system("cls")
    while True:
        print("""Menú mascota segura
        1.Grabar
        2.Buscar
        3.Retirarse
        4.Salir""")
def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion in(1,2,3,4,):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_nombre():
    while True:
        nom = input("Ingrese su nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
def validar_nombre_mascota():
    while True:
        nombre_mascota = input("Ingrese el nombre de su mascota: ")
        if len(nombre_mascota.strip()) >= 3 and nombre_mascota.isalpha():
            return nombre_mascota
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")                     
def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese número fila(1-6): "))
            if fila >= 1 and fila <= 6:
                return fila
            else:
                print("ERROR! FILA INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese número columna(1-12): "))
            if columna >= 1 and columna <= 12:
                return columna
            else:
                print("ERROR! COLUMNA INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
def id_unico():
    contador = 1 
    while True:
            id_unico = print (f"Su identificador unico es {contador+id_unico}")
def cantidad_dias():
    while True:
        try:
            cant_dias = int(input("Ingrese la cantidad de dias que estara su mascota"))
            if cant_dias > 1:
                return cant_dias
            else:
                print ("No podemos cuidar a su mascota por menos de un dia")
        except:
            print("¡ERROR! debe ingresar un valor valido")
def grabar():
    validar_rut()
    validar_nombre()
    id_unico()
    validar_nombre_mascota()
    cantidad_dias()
    lista_rut.append = []


def hotel():
    print("\tHOTEL CANINO\n")
    for x in range(2):
        for y in range(10):
            print([x] [y](x+1)(y+1))
    print()
def buscar():
    validar_rut()
    if validar_rut in lista_rut:
        print (hotel)
def retirarse():
    validar_rut()
    if validar_rut in lista_rut:
        pass


def salir():
    print ("Gracias por su visita")
    
