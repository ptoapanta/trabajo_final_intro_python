
def calcular_retorno_diario(precio_actual, precio_anterior):
    """
    Calcula el retorno diario a partir del precio actual y el precio anterior.

    Args:
        precio_actual (float): El precio actual.
        precio_anterior (float): El precio anterior.

    Returns:
        float: El retorno diario en porcentaje.
    """
    if precio_anterior == 0:
        raise ValueError("El precio anterior no puede ser cero.")
    return ((precio_actual - precio_anterior) / precio_anterior) * 100

def categorizar_volatilidad(desviacion_estandar):
    if desviacion_estandar < 2:
        return "Baja"
    elif 2 <= desviacion_estandar <= 5:
        return "Media"
    else:
        return "Alta"
