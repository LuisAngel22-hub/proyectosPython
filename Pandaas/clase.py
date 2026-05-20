class Estudiante():
    #inicia el constructor
    def __init__(self, nombres, semestres):  # Corregido de _init a _init_
        self.nombres = nombres
        self.semestres = semestres
    
    def saludar(self):
        print("Soy el estudiante:", self.nombres, "y curso en el semestre", self.semestres)
    
    def cambiarsemestre(self, semestres):
        self.semestres = semestres

maria = Estudiante("Maria", "I")
maria.saludar()  

juan = Estudiante("Juan","II")
juan.saludar()

juan.cambiarsemestre("IV")
juan.saludar()