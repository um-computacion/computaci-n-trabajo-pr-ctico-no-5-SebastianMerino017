import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from alumno import Alumno

class TestAlumno(unittest.TestCase):
    """Pruebas unitarias para la clase Alumno."""
    
    def test_crear_alumno(self):
        """Prueba la creación básica de un alumno."""
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.dni, "12345678")
        self.assertEqual(alumno.legajo, "A123")
    
    def test_repr_alumno(self):
        """Prueba la representación string de un alumno."""
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        expected = "Alumno: DNI: 12345678 Nombre: Juan Apellido: Pérez Legajo: A123"
        self.assertEqual(str(alumno), expected)
    
    def test_herencia_persona(self):
        """Prueba que el alumno hereda comportamientos de Persona."""
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        alumno.pensar("Estudiar para el examen")
        self.assertEqual(alumno.pensamientos, 1)
        self.assertEqual(alumno.ultima_idea, "Estudiar para el examen")