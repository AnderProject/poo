from abc import ABC, abstractclassmethod
from datetime import date, datetime

class Cliente:
    _secuencia = 0 
    def __init__(self,nombre,cedula,estado = True):
        Cliente._secuencia += 1
        self.__idCliente = Cliente._secuencia
        self.nombre = nombre
        self.cedula = cedula
        self.estado = estado

    @property
    def idCliente(self):
        return self.__idCliente
    
    def mostrarDatos(self):
        print(f"Nombre: {self.nombre} C.I: {self.cedula} Estado: {self.estado}")

cli1 = Cliente("Camila Pilligua", "0943336578",False)
cli1.mostrarDatos()

class Factura:
    _serie = 0
    def __init__(self,cliente,fecha,total,estado = True):
        Factura._serie += 1
        self.__idFactura = Factura._serie
        self.cliente = cliente
        self.fecha = fecha
        self.total = total
        self.estado = estado

    @property
    def idFactura(self):
        return self.__idFactura
    
    def mostrarDatos(self):
        print(f"Cliente: {self.cliente} Fecha: {self.fecha} Total: ${self.total} Estado:{self.estado}")

fac1 = Factura(cli1.nombre,"13/1/2023",3000,True)
fac1.mostrarDatos()


