import unittest
from guia7 import ordenados, vocales_distintas, iguales_consecutivos

class test_ordenados(unittest.TestCase):
    def test_ordenados(self):
        self.assertTrue(ordenados([1,3,7])) # para sec creciente.
    def test_ordenados_negativos(self):
        self.assertTrue(ordenados([-10, -5, -1]))
    def test_ordenados_mixtos(self):
        self.assertTrue(ordenados([-10, -5, 0, 1, 10]))
    def test_desordenados(self):
        self.assertFalse(ordenados([0, 4, 6, 1]))
    def test_desordenados_negativos(self):
        self.assertFalse(ordenados([-1, -5, -3]))

class test_vocales_distintas(unittest.TestCase):
    def test_tres_vocales_distintas(self):
        self.assertTrue(vocales_distintas(["aei"]))
    def test_sin_palabra(self):
        self.assertTrue(vocales_distintas([]))
    def test_vocales_iguales(self):
        self.assertFalse(vocales_distintas(["aaa"]))


    


if __name__ == "__main__": 
    unittest.main(verbosity=2)