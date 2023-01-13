from datetime import datetime,date
from empresa import Empresa
from cliente import ClienteCorporativo, ClientePersonal

class Articulo:
    _secuencia=0
    def __init__(self,des,pre,sto):
        Articulo._secuencia += 1
        self.__codigo = Articulo._secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = sto
    
    @property
    def codigo(self):
        return self.__codigo
        
    def mostrarArticulo(self):
        print(self.codigo,self.descripcion)
        

class DetalleVenta:
    _linea=0
    def __init__(self,articulo,cantidad):
        DetalleVenta._linea += 1
        self.linea = DetalleVenta._linea
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad = cantidad
        
class Venta:
    _factura=0
    _iva=0.12
    def __init__(self,cliente):
        Venta._factura = Venta._factura + 1
        self.factura = "F"+str(Venta._factura)
        self.fecha = date.today()
        self.cliente = cliente
        self.subtotal = 0
        self.iva = 0 
        self.total = 0
        self.detalleVenta = []
    
    def agregarDetalle(self,articulo,cantidad):
        detalle = DetalleVenta(articulo,cantidad)
        self.subtotal += round(detalle.precio*detalle.cantidad,2)
        self.iva = round(self.subtotal*Venta._iva,2)
        self.total = round(self.subtotal+self.iva,2)
        self.detalleVenta.append(detalle)    
    
    def mostrarVenta(self,empNombre,empRuc):
        print("Empresa: {:17} Ruc:{}".format(empNombre,empRuc))    
        print("Factura#:{:13}Fecha:  {}".format(self.factura,self.fecha))
        self.cliente.mostrarCliente()
        print("Linea Articulo     Precio Cantidad Subtotal")
        for det in self.detalleVenta:
            print("{:5} {:15} {} {:6} {:7}".format(det.linea,det.articulo.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))  
        print("*"*23,"Subtotal=> ",self.subtotal)
        print("*"*26,"Iva=> ",self.iva)
        print("*"*23,"Total=> ",self.total)    

empresa = Empresa()
cliente1 = ClienteCorporativo("Daniel","091422332","0912131415","da@gmail.com",False)      
cliente2 = ClienteCorporativo("Yady","091422332","0912131415","da@gmail.com",False)  
art1 = Articulo("Aceite",3,100)
art2 = Articulo("Coca Cola",1,200)
venta = Venta(cliente1)
venta.agregarDetalle(art1,3)
venta.agregarDetalle(art2,2)
venta.mostrarVenta(empresa.nombre,empresa.ruc)
