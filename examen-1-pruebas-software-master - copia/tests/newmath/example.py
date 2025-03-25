from tests.base import assert_equal

from newmath.example import saludar


def test_deberia_saludar_a_mundo():
    restultado: str = saludar("Mundo")
    esperado: str = "Hola, Mundo"
    assert_equal(esperado, restultado, "test_deberia_saludar_a_mundo")


def test_deberia_saludar_a_una_persona():
    restultado: str = saludar("Paco")
    esperado: str = "Hola, Paco"
    assert_equal(esperado, restultado, "test_deberia_saludar_a_una_persona")

def test_contar_vocales_deberia_contar_vocales_basicas():
    resultado: int = contar_vocales("Hola, cómo estás?")
    esperado: int = 7
    assert_equal(esperado, resultado, "test_contar_vocales_deberia_contar_vocales_basicas")

def test_contar_vocales_deberia_contar_todas_las_variantes():
    resultado: int = contar_vocales("AEIOUaeiouÁÉÍÓÚáéíóú")
    esperado: int = 20
    assert_equal(esperado, resultado, "test_contar_vocales_deberia_contar_todas_las_variantes")

def test_contar_vocales_deberia_retornar_cero_sin_vocales():
    resultado: int = contar_vocales("12345!@#")
    esperado: int = 0
    assert_equal(esperado, resultado, "test_contar_vocales_deberia_retornar_cero_sin_vocales")

def test_multiplicacion_vocales_deberia_calcular_correctamente():
    resultado: int = multiplicacion_vocales("aeiou")
    esperado: int = 9
    assert_equal(esperado, resultado, "test_multiplicacion_vocales_deberia_calcular_correctamente")

def test_multiplicacion_vocales_deberia_manejar_mayusculas():
    resultado: int = multiplicacion_vocales("Un murcielago")
    esperado: int = 4
    assert_equal(esperado, resultado, "test_multiplicacion_vocales_deberia_manejar_mayusculas")

def test_multiplicacion_vocales_deberia_manejar_vocales_acentuadas():
    resultado: int = multiplicacion_vocales("áéíóú")
    esperado: int = 20  # 5 vocales acentuadas * valor por defecto 4
    assert_equal(esperado, resultado, "test_multiplicacion_vocales_deberia_manejar_vocales_acentuadas")

def test_porcentaje_vocales_deberia_calcular_correctamente():
    resultado: float = porcentaje_vocales("Hola, cómo estás?")
    esperado: float = 46.15
    assert_equal(esperado, resultado, "test_porcentaje_vocales_deberia_calcular_correctamente")

def test_porcentaje_vocales_deberia_retornar_cero_sin_letras():
    resultado: float = porcentaje_vocales("12345!")
    esperado: float = 0.0
    assert_equal(esperado, resultado, "test_porcentaje_vocales_deberia_retornar_cero_sin_letras")

def test_porcentaje_vocales_deberia_manejar_solo_vocales():
    resultado: float = porcentaje_vocales("aeiou")
    esperado: float = 100.0
    assert_equal(esperado, resultado, "test_porcentaje_vocales_deberia_manejar_solo_vocales")