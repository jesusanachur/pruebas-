import unittest
from typing import Callable

def test_multiplicador_factor_todos_positivos_rango_medio():
    resultado = multiplicador_factor(5, 20, 50)
    esperado = 5*2 + 20*3 + 50*3  # 10 + 60 + 150
    assert_equal(esperado, resultado, "Números en rangos [0,10), [10,100), [10,100)")

def test_multiplicador_factor_con_negativo():
    resultado = multiplicador_factor(-3, 8, 15)
    esperado = -3*-1 + 8*2 + 15*3  # 3 + 16 + 45
    assert_equal(esperado, resultado, "Incluye número negativo")

def test_multiplicador_factor_numero_muy_grande():
    resultado = multiplicador_factor(150, 200, 1000)
    esperado = 150*4 + 200*4 + 1000*4  # 600 + 800 + 4000
    assert_equal(esperado, resultado, "Números >= 100 (factor 4)")

def test_multiplicador_factor_cero():
    resultado = multiplicador_factor(0, 0, 0)
    esperado = 0*2 + 0*2 + 0*2  # 0
    assert_equal(esperado, resultado, "Todos los números son 0")

def test_multiplicador_factor_mezcla_rangos():
    resultado = multiplicador_factor(-5, 9, 99)
    esperado = -5*-1 + 9*2 + 99*3  # 5 + 18 + 297
    assert_equal(esperado, resultado, "Mezcla de rangos [-∞,0), [0,10), [10,100)")

def test_multiplicador_factor_decimales():
    resultado = multiplicador_factor(3.5, 10.1, 99.9)
    esperado = 3.5*2 + 10.1*3 + 99.9*3  # 7.0 + 30.3 + 299.7
    assert_equal(esperado, resultado, "Números decimales en rangos válidos")

def test_multiplicador_factor_limite_inferior_rango():
    resultado = multiplicador_factor(0, 10, 100)
    esperado = 0*2 + 10*3 + 100*4  # 0 + 30 + 400
    assert_equal(esperado, resultado, "Límites exactos de rangos")

def test_multiplicador_factor_todos_negativos():
    resultado = multiplicador_factor(-1, -2, -3)
    esperado = -1*-1 + -2*-1 + -3*-1  # 1 + 2 + 3
    assert_equal(esperado, resultado, "Todos los números son negativos")

def test_multiplicador_factor_unico_rango_alto():
    resultado = multiplicador_factor(150, 150, 150)
    esperado = 150*4 + 150*4 + 150*4  # 1800
    assert_equal(esperado, resultado, "Todos los números >= 100")

def test_multiplicador_factor_mezcla_extremos():
    resultado = multiplicador_factor(-10, 9.999, 99.999)
    esperado = -10*-1 + 9.999*2 + 99.999*3  # 10 + 19.998 + 299.997
    assert_equal(round(esperado, 3), round(resultado, 3), "Valores en límites de rangos")



def test_factor_fibonacci_base_default():
    resultado = factor_fibonacci(5)
    esperado = 5 / 5  # 1.0 (secuencia: 0, 1, 1, 2, 3, 5)
    assert_equal(esperado, resultado, "Valores por defecto (a=0, b=1)")

def test_factor_fibonacci_base_personalizada():
    resultado = factor_fibonacci(6, 2, 3)
    esperado = round(34 / 6, 2)  # 5.67 (secuencia: 2, 3, 5, 8, 13, 21, 34)
    assert_equal(esperado, resultado, "Valores iniciales personalizados (a=2, b=3)")

def test_factor_fibonacci_n_igual_1():
    resultado = factor_fibonacci(1)
    esperado = 1 / 1  # 1.0 (secuencia: 0, 1)
    assert_equal(esperado, resultado, "n=1 con valores por defecto")

def test_factor_fibonacci_n_pequeno():
    resultado = factor_fibonacci(3, 1, 1)
    esperado = round(3 / 3, 2)  # 1.0 (secuencia: 1, 1, 2, 3)
    assert_equal(esperado, resultado, "n=3 con a=1, b=1")

def test_factor_fibonacci_n_grande():
    resultado = factor_fibonacci(10)
    esperado = round(55 / 10, 2)  # 5.5 (secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
    assert_equal(esperado, resultado, "n=10 con valores por defecto")


 

def test_factor_fibonacci_base_cero():
    resultado = factor_fibonacci(4, 0, 0)
    esperado = round(0 / 4, 2)  # 0.0 (secuencia: 0, 0, 0, 0, 0)
    assert_equal(esperado, resultado, "a=0 y b=0 (secuencia constante)")

def test_factor_fibonacci_base_negativa():
    resultado = factor_fibonacci(5, -1, -1)
    esperado = round(-5 / 5, 2)  # -1.0 (secuencia: -1, -1, -2, -3, -5, -8)
    assert_equal(esperado, resultado, "Valores iniciales negativos (a=-1, b=-1)")

def test_factor_fibonacci_redondeo_correcto():
    resultado = factor_fibonacci(7)
    esperado = round(13 / 7, 2)  # 1.86 (secuencia: 0, 1, 1, 2, 3, 5, 8, 13)
    assert_equal(esperado, resultado, "Verifica redondeo a 2 decimales")