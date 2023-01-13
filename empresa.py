class Empresa:
    def __init__(self,nom="Shopping car",ruc="0943213456001",tel="0992255432",dir="Milagro"):
        self.nombre=nom
        self.ruc=ruc
        self.tel=tel
        self.dir=dir

emp = Empresa()
print("__________________________")
print("empresa")
print(emp.nombre)

