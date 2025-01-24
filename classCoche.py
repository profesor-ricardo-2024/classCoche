class Coche:
    """
    Representa un coche con atributos básicos como marca, modelo, año, capacidad del tanque de combustible y nivel de combustible actual.
    
    Atributos:
        marca (str): La marca del coche.
        modelo (str): El modelo del coche.
        año (int): El año de fabricación del coche.
        capacidad_tanque (float): La capacidad del tanque de combustible en litros.
        nivel_combustible (float): El nivel actual de combustible en litros.
        velocidad (float): La velocidad actual del coche en km/h.
    """
    
    def __init__(self, marca, modelo, año, capacidad_tanque):
        """
        Inicializa una nueva instancia de la clase Coche.
        
        Parámetros:
            marca (str): La marca del coche.
            modelo (str): El modelo del coche.
            año (int): El año de fabricación del coche.
            capacidad_tanque (float): La capacidad del tanque de combustible en litros.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad_tanque = capacidad_tanque
        self.nivel_combustible = capacidad_tanque
        self.velocidad = 0

    def descripcion(self):
        """
        Devuelve una descripción del coche.
        
        Devuelve:
            str: Una cadena que describe el coche con su marca, modelo y año.
        """
        return f"{self.marca} {self.modelo} del año {self.año}"

    def arrancar(self):
        """
        Simula el arranque del coche. Verifica si hay suficiente combustible para arrancar.
        
        Devuelve:
            str: Un mensaje indicando si el coche ha arrancado o si falta combustible.
        """
        if self.nivel_combustible > 0:
            return f"{self.marca} {self.modelo} está arrancando..."
        else:
            return "No hay suficiente combustible para arrancar."

    def acelerar(self, incremento):
        """
        Aumenta la velocidad del coche y reduce el nivel de combustible.
        
        Parámetros:
            incremento (float): La cantidad en km/h a aumentar la velocidad.
        
        Devuelve:
            str: Un mensaje indicando la nueva velocidad del coche o si falta combustible.
        """
        if self.nivel_combustible > 0:
            self.velocidad += incremento
            self.nivel_combustible -= incremento * 0.05  # Consumo de combustible por aceleración
            return f"{self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h."
        else:
            return "No hay suficiente combustible para acelerar."

    def frenar(self, decremento):
        """
        Reduce la velocidad del coche.
        
        Parámetros:
            decremento (float): La cantidad en km/h a disminuir la velocidad.
        
        Devuelve:
            str: Un mensaje indicando la nueva velocidad del coche.
        """
        if self.velocidad >= decremento:
            self.velocidad -= decremento
            return f"{self.marca} {self.modelo} ha frenado a {self.velocidad} km/h."
        else:
            self.velocidad = 0
            return f"{self.marca} {self.modelo} ha frenado completamente."

    def verificar_combustible(self):
        """
        Verifica el nivel actual de combustible.
        
        Devuelve:
            str: Un mensaje indicando el nivel de combustible actual y la capacidad del tanque.
        """
        return f"Nivel de combustible: {self.nivel_combustible}/{self.capacidad_tanque} litros."

    def repostar(self, cantidad):
        """
        Añade combustible al tanque del coche.
        
        Parámetros:
            cantidad (float): La cantidad de combustible en litros a añadir.
        
        Devuelve:
            str: Un mensaje indicando el nuevo nivel de combustible o si la cantidad excede la capacidad del tanque.
        """
        if self.nivel_combustible + cantidad <= self.capacidad_tanque:
            self.nivel_combustible += cantidad
            return f"El tanque ha sido llenado con {cantidad} litros. Nivel actual: {self.nivel_combustible} litros."
        else:
            return "La cantidad excede la capacidad del tanque."

# Crear una instancia de la clase Coche
mi_coche = Coche("Renault", "Clio", 2004, 40)

# Usar los métodos de la clase
print(mi_coche.descripcion())               # Imprime: Renault Clio del año 2004
print(mi_coche.arrancar())                  # Imprime: Renault Clio está arrancando...
print(mi_coche.acelerar(20))                # Imprime: Renault Clio ha acelerado a 20 km/h.
print(mi_coche.verificar_combustible())     # Imprime: Nivel de combustible: 39.0/40 litros.
print(mi_coche.frenar(10))                  # Imprime: Renault Clio ha frenado a 10 km/h.
print(mi_coche.repostar(1))                 # Imprime: El tanque ha sido llenado con 1 litros. Nivel actual: 40.0 litros.

