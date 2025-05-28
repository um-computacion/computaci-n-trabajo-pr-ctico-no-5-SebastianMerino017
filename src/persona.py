class Persona:
    """Clase base que representa una persona con información básica.
    
    Attributes:
        nombre (str): Nombre de la persona.
        apellido (str): Apellido de la persona.
        dni (str): Documento Nacional de Identidad.
        pensamientos (int): Contador de pensamientos.
        ultima_idea (str): Último pensamiento registrado.
    """
    
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = "<no penso en nada>"
    
    def pensar(self, idea):
        """Registra un nuevo pensamiento."""
        
        self.pensamientos += 1
        self.ultima_idea = idea
    
    def __repr__(self):
        """Representa la persona como string."""
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
