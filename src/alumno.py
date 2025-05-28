from persona import Persona

class Alumno(Persona):
    """Clase que representa un alumno, heredando de Persona.
    
    Attributes:
        legajo (str): Legajo del alumno.
    """
    
    def __init__(self, nombre, apellido, dni, legajo):
        """Inicializa un nuevo alumno.
        
        Args:
            nombre (str): Nombre del alumno.
            apellido (str): Apellido del alumno.
            dni (str): Documento Nacional de Identidad.
            legajo (str): Legajo del alumno.
        """
        super().__init__(nombre, apellido, dni)
        self.legajo = legajo
    
    def __repr__(self):
        """Representa el alumno como string.
        
        Returns:
            str: Representación string del alumno.
        """
        return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"
