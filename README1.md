# Descripción del problema
Este repositorio contiene las implementaciones y pruebas de las siguientes funciones:
- Factorial (iterativa y recursiva)
- Fibonacci (iterativa y recursiva)
- Flatten (aplanar listas recursivamente)

# Instrucciones de ejecución
1. Clonar el repositorio o descargar el proyecto.

2. Desde la terminal, ubicarse en la carpeta raíz del proyecto.

3. Asegurarse de tener la siguiente estructura:
TP4/ 
    ├── src/ │ 
        ├── factorial.py  
        ├── fibonacci.py 
        ├── flatten.py  
        └── init.py 
    ├── tests/ │ 
        ├── test_factorial.py
        ├── test_fibonacci.py 
        ├── test_flatten.py  
        └── init.py 
    └── README.md
4. Ejecutar los tests con:

```bash
python3 -m unittest discover tests


# Ejemplos de uso

# Factorial
print(factorial_iterative(5))     # 120
print(factorial_recursive(4))     # 24

# Fibonacci
print(fibonacci_iterative(7))     # 13
print(fibonacci_recursive(6))     # 8

# Flatten
nested = [1, [2, 3], (4, 5), {'a': 6, 'b': [7, 8]}]
print(flatten(nested))  # [1, 2, 3, 4, 5, 'a', 6, 'b', 7, 8]


# Capturas de pantalla de los tests ejecutados

./tests_ok.png
