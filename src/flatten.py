def flatten(data):
    """
    Aplana listas anidadas, tuplas, diccionarios y listas combinadas.
    """
    result = []
    if isinstance(data, dict):
        for key, value in data.items():
            result.extend(flatten(key))
            result.extend(flatten(value))
    elif isinstance(data, (list, tuple)):
        for element in data:
            result.extend(flatten(element))
    else:
        result.append(data)
    return result
