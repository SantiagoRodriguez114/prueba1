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

    def salida(self, placa, iteraciones=0):
        if self.via.empty():
            print(f"Vehículo con placa {placa} no encontrado.")
            return iteraciones  

        vehiculo = self.via.get()
        iteraciones += 1  

        if vehiculo == placa:
            print(f"Vehículo con placa {placa} ha salido después de {iteraciones} movimientos.")
            return iteraciones  

        iteraciones = self.salida(placa, iteraciones)  

        self.via.put(vehiculo)  
        if not self.via.full() and not self.espera.empty():
            self.via.put(self.espera.get())
            
        return iteraciones  

    
    def mostrar(self):
        print("Estacionamiento:", list(self.via.queue))

    def mostrarEspera(self):
        print("Lista de espera:", list(self.espera.queue))
     
estacionamiento = Parqueo(3)

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


            


        
