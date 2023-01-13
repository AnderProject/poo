from abc import ABC,abstractmethod 
class Cliente(ABC):
    def __init__(self,nom,ced,tel,email):
         self.nombre = nom
         self.cedula = ced
         self.telefono = tel
         self.correo = email
  
    def validaCedula(self):
        if len(self.cedula) == 10:
            return self.cedula
        else:
            return None
    
    @abstractmethod 
    def mostrarCliente(self):
        pass

class ClienteCorporativo(Cliente):
    def __init__(self,nomb,cedu,tele,mail,contrato=True):
        super().__init__(nomb,cedu,tele,mail)
        self.__contrato= "Con Contato Vigente" if contrato else 'Sin Contrato Vigente'
        
        
    @property
    def contrato(self):  # getter: obtener el valor del atributo privado
        return self.__contrato
           
    def mostrarCliente(self):
       print(self.nombre,self.cedula,self.telefono,self.correo,self.contrato)     

class ClientePersonal(Cliente):
    def __init__(self,nom,ced,tel,mail,promocion=False):
        super().__init__(nom,ced,tel,mail)
        self.__promocion=promocion
        
    @property
    def promocion(self):  # getter: obtener el valor del atributo privado
        return self.__promocion
    
    def mostrarCliente(self):
        promocionPorcentaje = 10 if self.promocion else 0
        print("Cliente: {:13}Cedula: {} promocion: {}%".format(self.nombre,self.cedula,promocionPorcentaje))
      
if __name__ == '__main__':  
    print("________Clientes_________")       
    corporativo = ClienteCorporativo("Daniel","091422332","0912131415","da@gmail.com",False)
    personal = ClientePersonal("Evelyn","091422332","0912131415","da@gmail.com")
    corporativo.mostrarCliente()
    personal.mostrarCliente()

      