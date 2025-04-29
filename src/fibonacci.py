def fibonacci_iterative(n):
   
    if n < 0:
        raise ValueError("No se permiten números negativos")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursive(n):
  
    if n < 0:
        raise ValueError("No se permiten números negativos")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
