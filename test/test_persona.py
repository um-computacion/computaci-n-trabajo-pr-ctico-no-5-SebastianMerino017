import unittest
import sys
import os

# agregar el directorio src al path para importar las clases
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from persona import Persona

class TestPersona(unittest.TestCase):
    """Pruebas unitarias para la clase Persona."""
    
    def test_crear_persona(self):
        """Prueba la creación básica de una persona."""
        persona = Persona("Juan", "Pérez", "12345678")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellido, "Pérez")
        self.assertEqual(persona.dni, "12345678")
    
    def test_repr_persona(self):
        """Prueba la representación string de una persona."""
        persona = Persona("Juan", "Pérez", "12345678")
        expected = "Persona: DNI: 12345678 Nombre: Juan Apellido: Pérez Ultima Idea: <no penso en nada>"
        self.assertEqual(str(persona), expected)

    def test_pensar_incrementa_contador(self):
        """Prueba que pensar incrementa el contador de pensamientos."""
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.pensamientos, 1)
    
    def test_pensar_actualiza_ultima_idea(self):
        """Prueba que pensar actualiza la última idea."""
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.ultima_idea, "Hola mundo")
    
    def test_multiples_pensamientos(self):
        """Prueba múltiples pensamientos consecutivos."""
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Primer pensamiento")
        persona.pensar("Segundo pensamiento")
        self.assertEqual(persona.pensamientos, 2)
        self.assertEqual(persona.ultima_idea, "Segundo pensamiento")

    