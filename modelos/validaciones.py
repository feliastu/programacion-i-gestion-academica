"""Validaciones compartidas: se valida antes de modificar el atributo."""


def validar_texto(valor, campo):
    """Devuelve texto sin espacios extremos o informa un valor inválido."""
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} debe ser un texto no vacío.")
    return valor.strip()


def validar_entero_positivo(valor, campo):
    """No admite cero, negativos, decimales, cadenas ni booleanos."""
    if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:
        raise ValueError(f"{campo}: se requiere un número entero mayor que cero.")
    return valor


def validar_promedio(valor):
    """Aplica la escala de 0 a 5 adoptada para esta demostración."""
    if (isinstance(valor, bool) or not isinstance(valor, (int, float))
            or not 0 <= valor <= 5):
        raise ValueError("El promedio debe ser un número entre 0 y 5.")
    return float(valor)
