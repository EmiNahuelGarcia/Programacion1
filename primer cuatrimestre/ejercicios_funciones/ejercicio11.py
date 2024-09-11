def invertir_palabra(palabra):
    palabra_invertida = ""

    for i in palabra:
        palabra_invertida = i + palabra_invertida

    return palabra_invertida

def validar_palindromo(palabra):
    palabra_invertida = invertir_palabra(palabra)
    if palabra == palabra_invertida:
        return True
    else:
        return False


palabra = input("Ingrese la palabra que desea invertir: ").lower()

resultado = invertir_palabra(palabra)

print(resultado)

es_palindromo = validar_palindromo(palabra)
print(es_palindromo)