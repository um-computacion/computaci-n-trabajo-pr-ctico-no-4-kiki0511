def factorial_iterative(n):
    """
    Calcula el factorial de un número de forma iterativa
    """
    if n < 0:
        raise ValueError("el factorial no está definido para números negativos")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    calcula el factorial de un número de forma recursiva
    """
    if n < 0:
        raise ValueError("el factorial no está definido para números negativos")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
