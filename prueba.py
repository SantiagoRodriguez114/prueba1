import queue

class Parqueo:
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.via = queue.Queue(maxsize=capacidad)
        self.espera = queue.Queue()
            
    def entrada(self):
        placa = input('Ingrese la placa del vehiculo: ')

        if not self.via.full():
            
            self.via.put(placa)
            print('El vehiculo ha sido ingresado con exito')
        
        else: 
            self.espera.put(placa)
            print('El vehiculo ha sido puesto en espera, no hay espacio disponible...')

    def salida(self, placa):
        temp = queue.Queue()
        movimientos = 0  

        while not self.via.empty():
            vehiculo = self.via.get()
            movimientos += 1  

            if vehiculo == placa:
                print(f"Vehiculo con placa {placa} ha salido despues de {movimientos} movimientos.")
                break  
            temp.put(vehiculo)

        while not self.via.empty():
            temp.put(self.via.get())

        while not temp.empty():
            self.via.put(temp.get())

        if not self.via.full() and not self.espera.empty():
            self.via.put(self.espera.get())  

    
    def mostrar(self):
        print("Estacionamiento:", end=" ")
        for i in range(self.via.qsize()):
            vehiculo = self.via.get()
            print(vehiculo, end=" ")
            self.via.put(vehiculo)
        print()

    def mostrarEspera(self):
        print("Lista de espera:", end=" ")
        for i in range(self.espera.qsize()):
            vehiculo = self.espera.get()
            print(vehiculo, end=" ")
            self.espera.put(vehiculo)
        print()
     
estacionamiento = Parqueo(8)

while True:
    print("\n----------------------")
    print("1. Ingresar vehiculo.")
    print("2.Sacar vehiculo.")
    print("3.Mostrar estacionamiento")
    print("4.Mostrar lista de espera")
    print("5. Salir")

    opc = input("Seleccione una opcion: ")

    match opc:
        case "1":
            estacionamiento.entrada()
        case "2":
            placa = input("Ingrese la placa del vehiculo: ")
            estacionamiento.salida(placa)
        case "3":
            estacionamiento.mostrar()
        case "4":
            estacionamiento.mostrarEspera()
        case "5":
            print("Saliendo...")
            break
        case _ : print("Ingresa una opcion valida...")
