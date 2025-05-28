from persona import Persona

class Profesor(Persona):
    """Clase que representa un profesor, heredando de Persona.
    
    Attributes:
        sueldo (float): Sueldo del profesor.
    """
    
    def __init__(self, nombre, apellido, dni, sueldo):
        """Inicializa un nuevo profesor.
        
        Args:
            nombre (str): Nombre del profesor.
            apellido (str): Apellido del profesor.
            dni (str): Documento Nacional de Identidad.
            sueldo (float): Sueldo del profesor.
        """
        super().__init__(nombre, apellido, dni)
        self.sueldo = sueldo
    
    def __repr__(self):
        """Representa el profesor como string.
        
        Returns:
            str: Representación string del profesor.
        """
        return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo}"