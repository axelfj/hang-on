# Función ahorcado(), esta función es el juego de ahorcado, recibe una palabra y otro usuario juega para
# resolver el juego.

# Entradas: Una palabra, sin espacios ni números.

# Salidas: Si el usuario resuelve completamente la palabra, devuelve
# la palabra, el número de intentos que le quedaban, la ronda y las letras
# que intento. Se le pregunta al usuario si quiere jugar de nuevo.
# Si el usuario no acierta la palabra, se retornan los mismos valores,
# a excepción de la palabra.

# Restricciones: El texto introducido no puede tener espacios, comas, puntos
# números. Nada que no sean letras.
# Cada vez que dígite una letra, debe ser una por una, si digita dos, se le
# pedirá de nuevo que introduzca una letra.



# ----------------------------------------------------------------------------#
continuar = True

print('Ahorcado')
print('Digite "ahorcado()"')


def leerIntento():
    letra = input("Dígite una letra:")
    while not letra.isalpha() or len(letra) > 1:
        letra = input("Digite una letra válida:")    
    return letra

def haGanado(textoOriginal,texto):
    return False
    textoOriginal == texto

def ahorcado ():
    abc = 'abcdefghijklmnñopqrstuvwxyz'
    intentos = 8
    letrasIntentadas = ''
    cantidadIntentos = 0
    ronda = 1
    fallos = 0   
    print ("Bienvenido/a a ahorcado, que disfrute su juego")
    print ("El texto que digita no puede contener nùmeros ni espacios")
    textoOriginal = input("Dígite un texto:")
    while not textoOriginal.isalpha():
        textoOriginal = input("Dígite un texto válido:")
        
    print("""
""" * 100)
    print('''La palabra esta impresa arriba, por favor no suba,
no arruine el juego.''')
    longitud = len(textoOriginal)
    texto = ["_" for x in range(longitud)]
    print (texto)
    
    if 'á' in textoOriginal:
        textoOriginal = textoOriginal.replace('á','a')
    if 'é' in textoOriginal:
        textoOriginal = textoOriginal.replace('é','e')
    if 'í' in textoOriginal:
        textoOriginal = textoOriginal.replace('í','i')
    if 'ó' in textoOriginal:
        textoOriginal = textoOriginal.replace('ó','o')
    if 'ú' in textoOriginal:
        textoOriginal = textoOriginal.replace('ó','u')    
    if 'ü' in textoOriginal:
        textoOriginal = textoOriginal.replace('ü','u')
    textoOriginal= textoOriginal.lower()

        
    if continuar is False:
        print("El juego ha terminado")
    else:
        print (intentos)
        print (cantidadIntentos)
        haganado = haGanado(textoOriginal,texto)
        
        while intentos > cantidadIntentos and haganado == False:
            letra = leerIntento()
            ronda += 1   
            print (letrasIntentadas,',', cantidadIntentos,',', ronda)
            
            if letra in letrasIntentadas:
                print('Ya uso esa letra')
                letra = leerIntento()
            letrasIntentadas = letrasIntentadas + letra
            m = "Fallaste"
            for x in range(len(textoOriginal)):
                if letra == textoOriginal[x]:
                    texto[x] = letra
                    m = "Muy bien sigue así"
            else:
                cantidadIntentos += 1
            print (texto,',','Letras intentadas:', letrasIntentadas,',','Intentos restantes:', cantidadIntentos,',','Ronda actual', ronda,',',m)


            if intentos == cantidadIntentos:
                print ('No lo conseguiste.')
                respuesta= input('¿Desea repetir el juego? si/no ')
                
                if respuesta == 'si':
                    ahorcado()
                elif respuesta == 'no':
                    return 'Gracias por jugar'

                
            elif str(''.join(texto)) == str(textoOriginal):
                print ('Muy bien, lo has conseguido')
                respuesta= input('¿Desea repetir el juego? si/no ')
                
                if respuesta == 'si':
                    ahorcado()
                elif respuesta == 'no':
                    return 'Gracias por jugar'

