def binario_parte_entero(numero):
    binario = ""
    while int(numero) > 0:
        binario = str(int(numero) % 2) + binario
        numero = int(numero) // 2
    return binario
def octal_parte_entera(numero):
    octal = ''
    while int(numero) > 0:
        digito = int(numero) % 8
        octal = str(digito) + octal
        numero = int(numero) // 8
    return octal
def hexadecimal_parte_entero(numero):
    hexadecimal = ''
    mapeo_hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while int(numero) > 0:
        digito = int(numero) % 16
        if int(digito) > 9:
            digito_hex = mapeo_hex[int(digito)]
        else:
            digito_hex = str(digito)
        hexadecimal = digito_hex + hexadecimal
        numero = int(numero) // 16
    return hexadecimal

def menu_conversion_decimal(numero):
    print("1. Binario")
    print("2. Octal")
    print("3. Hexadecimal")
    opcion = int(input("\nConvertir a: "))
    if opcion==1:
        if '.' in str(numero):
            parte_entera, parte_fraccion = str(numero).split(".")
            parte_fraccion = float("0." + parte_fraccion)
        else:
            parte_entera = str(numero)
            parte_fraccion = 0
        parte_entera = int(parte_entera)
        binario_entero = binario_parte_entero(parte_entera)
        binario_fraccion = ""
        if parte_fraccion > 0:
            while parte_fraccion > 0 and len(binario_fraccion) <= 10:
                parte_fraccion *= 2
                if parte_fraccion >= 1:
                    binario_fraccion += '1'
                    parte_fraccion -= 1
                else:
                    binario_fraccion += '0'
            resultado = binario_entero + "." + binario_fraccion
        else:
            resultado = binario_entero
        print(f"El número decimal {numero} en binario es: {resultado}\n\n")
    elif opcion==2:
        if '.' in str(numero):
            parte_entera, parte_fraccion = str(numero).split(".")
            parte_fraccion = float("0." + parte_fraccion)
        else:
            parte_entera = str(numero)
            parte_fraccion = 0
        parte_entera = int(parte_entera)
        octal_entero = octal_parte_entera(parte_entera)
        octal_fraccion = ""
        if parte_fraccion > 0:
            while parte_fraccion > 0 and len(octal_fraccion) <= 10:  # Limitar la longitud para evitar bucle infinito
                parte_fraccion *= 8
                octal_fraccion += str(int(parte_fraccion))
                parte_fraccion -= int(parte_fraccion)
            resultado = octal_entero + "." + octal_fraccion
        else:
            resultado = octal_entero
        print(f"El número decimal {numero} en octal es: {resultado}\n\n")
    elif opcion==3:
        if '.' in str(numero):
            parte_entera, parte_fraccion = str(numero).split(".")
            parte_fraccion = float("0." + parte_fraccion)
        else:
            parte_entera = str(numero)
            parte_fraccion = 0
        parte_entera = int(parte_entera)
        hexadecimal_entero = hexadecimal_parte_entero(parte_entera)
        hexadecimal_fraccion = ""
        if parte_fraccion > 0:
            while parte_fraccion > 0 and len(hexadecimal_fraccion) <= 10:
                parte_fraccion *= 16
                hexadecimal_fraccion += format(int(parte_fraccion), 'x')
                parte_fraccion -= int(parte_fraccion)
            resultado = hexadecimal_entero + "." + hexadecimal_fraccion
        else:
            resultado = hexadecimal_entero
        print(f"El número decimal {numero} en hexadecimal es: {resultado}\n\n")

def menu_conversion_binario(numero):
    print("1. Decimal")
    print("2. Octal")
    print("3. Hexadecimal")
    opcion = int(input("\nConvertir a: "))
    if opcion==1:
        if '.' in numero:
            parte_entera, parte_fraccion = numero.split(".")
        else:
            parte_entera = numero
            parte_fraccion = ''
        decimal_entero = 0
        for digito in parte_entera:
            decimal_entero = decimal_entero * 2 + int(digito)
        decimal_fraccion = 0
        potencia = -1
        for digito in parte_fraccion:
            decimal_fraccion += int(digito) * (2 ** potencia)
            potencia -= 1
        resultado = decimal_entero + decimal_fraccion
        print(f"El número binario {numero} en decimal es: {resultado}\n\n")
    elif opcion==2:
        bin_a_oct = {
        '000': '0', '001': '1', '010': '2', '011': '3',
        '100': '4', '101': '5', '110': '6', '111': '7'}
        if '.' in numero:
            partes = numero.split('.')
            parte_entera = partes[0]
            parte_fraccionaria = partes[1]
        else:
            parte_entera = numero
            parte_fraccionaria = ''
        while len(parte_entera) % 3 != 0:
            parte_entera = '0' + parte_entera
        octal_entero = ''
        for i in range(0, len(parte_entera), 3):
            tres_bits = parte_entera[i:i+3]
            octal_entero += bin_a_oct[tres_bits]
        octal_fraccionario = ''
        if parte_fraccionaria:
            while len(parte_fraccionaria) % 3 != 0:
                parte_fraccionaria += '0'
            for i in range(0, len(parte_fraccionaria), 3):
                tres_bits = parte_fraccionaria[i:i+3]
                octal_fraccionario += bin_a_oct[tres_bits]
        octal = octal_entero
        if octal_fraccionario:
            octal += '.' + octal_fraccionario
        print(f"El número binario {numero} en octal es: {octal}\n\n")
    elif opcion==3:
        bin_a_hex = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
        if '.' in numero:
            partes = numero.split('.')
            parte_entera = partes[0]
            parte_fraccionaria = partes[1]
        else:
            parte_entera = numero
            parte_fraccionaria = ''
        while len(parte_entera) % 4 != 0:
            parte_entera = '0' + parte_entera
        hexadecimal_entero = ''
        for i in range(0, len(parte_entera), 4):
            cuatro_bits = parte_entera[i:i+4]
            hexadecimal_entero += bin_a_hex[cuatro_bits]
        hexadecimal_fraccionario = ''
        if parte_fraccionaria:
            while len(parte_fraccionaria) % 4 != 0:
                parte_fraccionaria += '0'
            for i in range(0, len(parte_fraccionaria), 4):
                cuatro_bits = parte_fraccionaria[i:i+4]
                hexadecimal_fraccionario += bin_a_hex[cuatro_bits]
        hexadecimal = hexadecimal_entero
        if hexadecimal_fraccionario:
            hexadecimal += '.' + hexadecimal_fraccionario
        print(f"El número binario {numero} en hexadecimal es: {hexadecimal}\n\n")


def menu_conversion_octal(numero):
    print("1. Decimal")
    print("2. Binario")
    print("3. Hexadecimal")
    opcion = int(input("\nConvertir a: "))
    if opcion==1:
        if '.' in numero:
            parte_entera, parte_fraccion = numero.split(".")
        else:
            parte_entera = numero
            parte_fraccion = ''
        decimal_entero = 0
        longitud_entera = len(parte_entera)
        for i in range(longitud_entera):
            digito = int(parte_entera[longitud_entera - i - 1])
            decimal_entero += digito * (8 ** i)
        decimal_fraccion = 0
        for i in range(len(parte_fraccion)):
            digito = int(parte_fraccion[i])
            decimal_fraccion += digito * (8 ** -(i + 1))
        resultado = decimal_entero + decimal_fraccion
        print(f"El número octal {numero} en decimal es: {resultado}\n\n")
    elif opcion==2:
        octal_a_binario_map = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'}
        if '.' in numero:
            parte_entera, parte_fraccion = numero.split(".")
        else:
            parte_entera = numero
            parte_fraccion = ''
        binario_entero = ''
        for digito in parte_entera:
            binario_entero += octal_a_binario_map[digito]
        binario_fraccion = ''
        for digito in parte_fraccion:
            binario_fraccion += octal_a_binario_map[digito]
        binario = binario_entero
        if parte_fraccion:
            binario += '.' + binario_fraccion
        print(f"El número octal {numero} en binario es: {binario}\n\n")

    elif opcion==3:
        if '.' in numero:
            parte_entera, parte_fraccion = numero.split(".")
        else:
            parte_entera = numero
            parte_fraccion = ''
        decimal_entero = 0
        longitud_entera = len(parte_entera)
        for i in range(longitud_entera):
            digito = int(parte_entera[longitud_entera - i - 1])
            decimal_entero += digito * (8 ** i)
        decimal_fraccion = 0
        for i in range(len(parte_fraccion)):
            digito = int(parte_fraccion[i])
            decimal_fraccion += digito * (8 ** -(i + 1))
        resultado = decimal_entero + decimal_fraccion
        if '.' in str(resultado):
            parte_entera, parte_fraccion = str(resultado).split(".")
            parte_fraccion = float("0." + parte_fraccion)
        else:
            parte_entera = str(resultado)
            parte_fraccion = 0
        parte_entera = int(parte_entera)
        hexadecimal_entero = hexadecimal_parte_entero(parte_entera)
        hexadecimal_fraccion = ""
        if parte_fraccion > 0:
            while parte_fraccion > 0 and len(hexadecimal_fraccion) <= 10:
                parte_fraccion *= 16
                hexadecimal_fraccion += format(int(parte_fraccion), 'X')
                parte_fraccion -= int(parte_fraccion)
            resultado = hexadecimal_entero + "." + hexadecimal_fraccion
        else:
            resultado = hexadecimal_entero
        print(f"El número octal {numero} en hexadecimal es: {resultado}\n\n")


def menu_conversion_hexadecimal(numero):
    print("1. Decimal")
    print("2. Binario")
    print("3. Octal")
    opcion = int(input("\nConvertir a: "))
    if opcion==1:
        hex_a_dec_map = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'a': 10, 'b': 11, 'c': 12, 'd': 13,
        'e': 14, 'f': 15}
        decimal = 0
        if '.' in numero:
            parte_entera, parte_fraccion = numero.split('.')
        else:
            parte_entera, parte_fraccion = numero, ''
        for i, digito in enumerate(parte_entera[::-1]):
            decimal += hex_a_dec_map[digito] * (16 ** i)
        for i, digito in enumerate(parte_fraccion):
            decimal += hex_a_dec_map[digito] * (16 ** -(i+1))
        print(f"El número hexadecimal {numero} en decimal es: {decimal}\n\n")
    elif opcion==2:
        hex_a_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
        'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101',
        'e': '1110', 'f': '1111'}
        if '.' in numero:
            parte_entera, parte_fraccion = numero.split('.')
        else:
            parte_entera, parte_fraccion = numero, ''
        binario_entero = ""
        binario_fraccion = ""
        for digito in parte_entera:
            binario_entero += hex_a_bin_map[digito]
        if parte_fraccion:
            for digito in parte_fraccion:
                binario_fraccion += hex_a_bin_map[digito]
            binario_fraccion = '.' + binario_fraccion
        binario = binario_entero + binario_fraccion
        print(f"El número hexadecimal {numero} en binario es: {binario}\n\n")
    elif opcion==3:
        hex_a_dec_map = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'a': 10, 'b': 11, 'c': 12, 'd': 13,
        'e': 14, 'f': 15}
        decimal = 0
        if '.' in numero:
            parte_entera, parte_fraccion = numero.split('.')
        else:
            parte_entera, parte_fraccion = numero, ''
        for i, digito in enumerate(parte_entera[::-1]):
            decimal += hex_a_dec_map[digito] * (16 ** i)
        for i, digito in enumerate(parte_fraccion):
            decimal += hex_a_dec_map[digito] * (16 ** -(i+1))
        if '.' in str(decimal):
            parte_entera, parte_fraccion = str(decimal).split(".")
            parte_fraccion = float("0." + parte_fraccion)
        else:
            parte_entera = str(decimal)
            parte_fraccion = 0
        parte_entera = int(parte_entera)
        octal_entero = octal_parte_entera(parte_entera)
        octal_fraccion = ""
        if parte_fraccion > 0:
            while parte_fraccion > 0 and len(octal_fraccion) <= 10:
                parte_fraccion *= 8
                octal_fraccion += str(int(parte_fraccion))
                parte_fraccion -= int(parte_fraccion)
            octal = octal_entero + "." + octal_fraccion
        else:
            octal = octal_entero
        print(f"El número hexadecimal {numero} en octal es: {octal}\n\n")



opcion = None
while opcion != 5:
    print("1. Decimal")
    print("2. Binario")
    print("3. Octal")
    print("4. Hexadecimal")
    print("5. Salir")
    opcion = int(input("Selecciona la base del número a convertir: "))
    if opcion==5:
        break
    numero = input("Dame el numero a convertir: ")
    if opcion==1:
        menu_conversion_decimal(numero)
    elif opcion==2:
        menu_conversion_binario(numero)
    elif opcion==3:
        menu_conversion_octal(numero)
    elif opcion==4:
        menu_conversion_hexadecimal(numero)