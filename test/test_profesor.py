import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from profesor import Profesor

class TestProfesor(unittest.TestCase):
    """Pruebas unitarias para la clase Profesor."""
    
    def test_crear_profesor(self):
        """Prueba la creación básica de un profesor."""
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        self.assertEqual(profesor.nombre, "Juan")
        self.assertEqual(profesor.apellido, "Pérez")
        self.assertEqual(profesor.dni, "12345678")
        self.assertEqual(profesor.sueldo, 50000)
    
    def test_repr_profesor(self):
        """Prueba la representación string de un profesor."""
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        expected = "Profesor: DNI: 12345678 Nombre: Juan Apellido: Pérez Sueldo: 50000"
        self.assertEqual(str(profesor), expected)
    
    def test_herencia_persona(self):
        """Prueba que el profesor hereda comportamientos de Persona."""
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        profesor.pensar("Preparar clase")
        self.assertEqual(profesor.pensamientos, 1)
        self.assertEqual(profesor.ultima_idea, "Preparar clase")