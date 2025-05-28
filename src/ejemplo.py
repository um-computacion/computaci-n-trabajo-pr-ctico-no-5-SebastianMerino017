from persona import Persona
from profesor import Profesor
from alumno import Alumno

def main():
    """Ejemplo de uso del sistema de gestión de personas."""
    
    print("=== Sistema de Gestión de Personas ===\n")
    
    # Crear una persona común
    persona = Persona("Ana", "García", "87654321")
    print("1. Persona creada:")
    print(persona)
    
    # Hacer que la persona piense
    persona.pensar("Qué lindo día")
    print(f"Después de pensar: {persona}")
    print(f"Cantidad de pensamientos: {persona.pensamientos}\n")
    
    # Crear un profesor
    profesor = Profesor("Carlos", "Rodríguez", "11223344", 75000)
    print("2. Profesor creado:")
    print(profesor)
    
    # El profesor también puede pensar
    profesor.pensar("Debo preparar la clase de mañana")
    print(f"Profesor pensando: {profesor.ultima_idea}")
    print(f"Pensamientos del profesor: {profesor.pensamientos}\n")
    
    # Crear un alumno
    alumno = Alumno("María", "López", "55667788", "EST2024001")
    print("3. Alumno creado:")
    print(alumno)
    
    # El alumno también puede pensar
    alumno.pensar("Tengo que estudiar más Python")
    print(f"Alumno pensando: {alumno.ultima_idea}")
    print(f"Pensamientos del alumno: {alumno.pensamientos}\n")
    
    # Demostrar polimorfismo
    print("4. Demostrando polimorfismo:")
    personas = [persona, profesor, alumno]
    
    for i, p in enumerate(personas, 1):
        p.pensar(f"Pensamiento número {i}")
        print(f"Persona {i}: {p}")
    
    print("\n=== Fin del ejemplo ===")

if __name__ == "__main__":
    main()