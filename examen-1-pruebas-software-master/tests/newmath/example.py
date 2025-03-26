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

