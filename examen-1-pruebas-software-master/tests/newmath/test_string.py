def test_contar_vocales_solo_una_vocal(self):
    resultado = contar_vocales("a")
    esperado = 1
    self.assert_equal(esperado, resultado, "Debe contar 1 vocal en texto de un solo carácter")

def test_contar_vocales_con_ñ_y_consonantes(self):
    resultado = contar_vocales("ñÑbcdfg")
    esperado = 0
    self.assert_equal(esperado, resultado, " debe retornar 0")

def test_contar_vocales_con_vocales_mayusculas_no_acentuadas(self):
    resultado = contar_vocales("AEIOU")
    esperado = 5
    self.assert_equal(esperado, resultado, "Debe contar vocales mayúsculas ")

def test_contar_vocales_con_vocales_minusculas_no_acentuadas(self):
    resultado = contar_vocales("aeiou")
    esperado = 5
    self.assert_equal(esperado, resultado, "Debe contar vocales minúsculas sin acento")

def test_contar_vocales_con_mezcla_mayusculas_minusculas(self):
    resultado = contar_vocales("aEiOu")
    esperado = 5
    self.assert_equal(esperado, resultado, "Debe contar vocales mezclando mayúsculas/minúsculas")

def test_contar_vocales_con_espacios_y_puntuacion(self):
    resultado = contar_vocales("a , e , i , o , u")
    esperado = 5
    self.assert_equal(esperado, resultado, "Debe ignorar espacios y puntuación")

def test_contar_vocales_con_vocales_acentuadas_mayusculas(self):
    resultado = contar_vocales("ÁÉÍÓÚ")
    esperado = 5
   self.assert_equal(esperado, resultado, "Debe contar vocales mayúsculas acentuadas")

def test_contar_vocales_con_vocales_acentuadas_minusculas(self):
    resultado = contar_vocales("áéíóú")
    esperado = 5
    self.assert_equal(esperado, resultado, "Debe contar vocales minúsculas acentuadas")

def test_contar_vocales_con_caracteres_especiales(self):
    resultado = contar_vocales("@#a$%e^&")
    esperado = 2
    self.assert_equal(esperado, resultado, "Debe ignorar caracteres especiales")

def test_contar_vocales_con_numeros(self):
    resultado = contar_vocales("1a2e3i4o5u")
    esperado = 5
    self.assert_equal(esperado, resultado, "Debe ignorar números")

def test_multiplicacion_vocales_con_una_sola_vocal(self):
    resultado = multiplicacion_vocales("a")
    esperado = 3
    self.assert_equal(esperado, resultado, "Una vocal 'a' debe retornar 3")

def test_multiplicacion_vocales_con_vocal_mayuscula(self):
    resultado = multiplicacion_vocales("A")
    esperado = -4
    self.assert_equal(esperado, resultado, "Vocal mayúscula 'A' debe retornar -4")

def test_multiplicacion_vocales_con_mezcla_valores_positivos_negativos(self):
    resultado = multiplicacion_vocales("aAeE")
    esperado = 2
    self.assert_equal(esperado, resultado, "a=3 + A=-4 + e=5 + E=-2 debe sumar 2")

def test_multiplicacion_vocales_con_repeticion_de_vocal(self):
    resultado = multiplicacion_vocales("aaa")
    esperado = 9
    self.assert_equal(esperado, resultado, "Tres 'a' deben sumar 9 (3x3)")

def test_multiplicacion_vocales_con_vocal_u_mayuscula(self):
    resultado = multiplicacion_vocales("U")
    esperado = -5
    self.assert_equal(esperado, resultado, "Vocal 'U' debe retornar -5")

def test_multiplicacion_vocales_con_palabra_compleja(self):
    resultado = multiplicacion_vocales("Murciélago")
    esperado = 8  
    self.assert_equal(esperado, resultado,)

def test_multiplicacion_vocales_con_vocales_acentuadas(self):
    resultado = multiplicacion_vocales("áéíóú")
    esperado = 20
    self.assert_equal(esperado, resultado,)

def test_multiplicacion_vocales_con_caracteres_no_alfabeticos(self):
    resultado = multiplicacion_vocales("a1e2i3o4u5")
    esperado = 9
    self.assert_equal(esperado, resultado, )

def test_multiplicacion_vocales_con_espacios(self):
    resultado = multiplicacion_vocales("a e i o u")
    esperado = 9
    self.assert_equal(esperado, resultado, "Debe ignorar espacios")

def test_multiplicacion_vocales_con_solo_consonantes(self):
    resultado = multiplicacion_vocales("bcdfg")
    esperado = 0
    self.assert_equal(esperado, resultado, "Sin vocales debe retornar 0")    



def test_porcentaje_vocales_con_una_sola_vocal(self):
    resultado = porcentaje_vocales("a")
    esperado = 100.0
    self.assert_equal(esperado, resultado, "Texto con una vocal debe retornar 100%")

def test_porcentaje_vocales_con_una_sola_consonante(self):
    resultado = porcentaje_vocales("b")
    esperado = 0.0
    self.assert_equal(esperado, resultado, "Texto con una consonante debe retornar 0%")

def test_porcentaje_vocales_con_mitad_vocales(self):
    resultado = porcentaje_vocales("a1b2c3d4e5")
    esperado = 40.0
    self.assert_equal(esperado, resultado, "2 vocales en 5 letras debe retornar 40%")

def test_porcentaje_vocales_con_todas_vocales(self):
    resultado = porcentaje_vocales("aeiou")
    esperado = 100.0
    self.assert_equal(esperado, resultado, "Texto con solo vocales debe retornar 100%")

def test_porcentaje_vocales_con_todas_consonantes(self):
    resultado = porcentaje_vocales("bcdfg")
    esperado = 0.0
    self.assert_equal(esperado, resultado, "Texto sin vocales debe retornar 0%")

def test_porcentaje_vocales_con_vocales_acentuadas(self):
    resultado = porcentaje_vocales("áéíóú")
    esperado = 100.0
    self.assert_equal(esperado, resultado, "Vocales acentuadas cuentan como vocales")

def test_porcentaje_vocales_con_espacios_y_puntuacion(self):
    resultado = porcentaje_vocales("a b c d e")
    esperado = 40.0
    self.assert_equal(esperado, resultado, "Espacios no cuentan como letras")

def test_porcentaje_vocales_con_numeros_y_simbolos(self):
    resultado = porcentaje_vocales("1a2b3c4d5e6")
    esperado = 40.0
    self.assert_equal(esperado, resultado, "Debe ignorar números y símbolos")

def test_porcentaje_vocales_con_mayusculas_y_minusculas(self):
    resultado = porcentaje_vocales("AaEeIiOoUu")
    esperado = 100.0
    self.assert_equal(esperado, resultado, "Mayúsculas/minúsculas cuentan igual")

def test_porcentaje_vocales_con_caracteres_especiales(self):
    resultado = porcentaje_vocales("@a#b$c%d^e&")
    esperado = 40.0
   self.assert_equal(esperado, resultado, "Debe ignorar caracteres especiales")