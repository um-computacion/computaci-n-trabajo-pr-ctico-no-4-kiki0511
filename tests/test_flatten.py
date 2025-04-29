import unittest
from src.flatten import flatten

class TestFlatten(unittest.TestCase):
    def test_lista_simple(self):
        lista = [1, 2, 3, 4]
        resultado = [1, 2, 3, 4]
        self.assertEqual(flatten(lista), resultado)

    def test_lista_anidada(self):
        lista = [1, [2, 3], [4, [5, 6]]]
        resultado = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten(lista), resultado)

    def test_lista_mixta(self):
        lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
        resultado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
        self.assertEqual(flatten(lista), resultado)

if __name__ == "__main__":
    unittest.main()
