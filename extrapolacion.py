def metodo_basico(tarjeta):
    return tarjeta[:6] + 'x' * 10

def metodo_similitud(tarjeta1, tarjeta2):
    resultado = tarjeta1[:6]  # Conserva los primeros 6 dígitos
    for d1, d2 in zip(tarjeta1[6:], tarjeta2[6:]):
        resultado += d1 if d1 == d2 else 'x'  # Extrapolación
    return resultado

def metodo_activacion(tarjeta):
    return tarjeta[:10] + 'x' * 6

def metodo_identacion_logica(tarjeta):
    primeros_seis_digitos = tarjeta[:6]  # Conserva los primeros 6 dígitos

    # Toma los dígitos restantes (10 dígitos) y los divide en grupos (3-4-3)
    grupo_1 = tarjeta[6:9]
    grupo_2 = tarjeta[9:13]
    grupo_3 = tarjeta[13:]

    # Aplica la extrapolación en cada grupo
    grupo_1 = grupo_1[:1] + 'x' + grupo_1[2:]  # Grupo de 3 dígitos
    grupo_2 = grupo_2[:1] + 'x' * 2 + grupo_2[3:]  # Grupo de 4 dígitos
    grupo_3 = grupo_3[:1] + 'x' + grupo_3[2:]  # Grupo de 3 dígitos

    # Combina los grupos modificados y ajusta a 16 dígitos, eliminando las últimas 6 'x'
    resultado_grupo = grupo_1 + grupo_2 + grupo_3
    resultado_grupo = resultado_grupo[:10].ljust(16, ' ')

    return primeros_seis_digitos + resultado_grupo

def metodo_sofia(cc1, cc2):
    grupo1_cc1, grupo2_cc1 = cc1[:8], cc1[8:]
    grupo1_cc2, grupo2_cc2 = cc2[:8], cc2[8:]

    # Multiplicación de los dígitos del primer grupo de CC2 con CC1
    resultado_multiplicacion = ''
    for d1, d2 in zip(grupo1_cc1, grupo1_cc2):
        resultado_multiplicacion += str(int(d1) * int(d2))

    # Ajustar a 8 dígitos
    resultado_multiplicacion = resultado_multiplicacion[:8]

    # Concatenar el primer grupo de CC1 con el resultado de la multiplicación
    resultado_cc = grupo1_cc1 + resultado_multiplicacion

    # Extrapolación usando SIMILITUD entre CC1 y el resultado
    resultado_extrapolado = ''
    for d1, d2 in zip(cc1, resultado_cc):
        if d1 == d2:
            resultado_extrapolado += d1
        else:
            resultado_extrapolado += 'x'

    # Reemplazar la última 'x' por '1' si es necesario
    if resultado_extrapolado[-1] == 'x':
        resultado_extrapolado = resultado_extrapolado[:-1] + '1'

    return resultado_extrapolado

# Abre el archivo 'tarjetas.txt' en modo lectura
with open('C:/Users/yourname/Desktop/BOT EXTRAPOLACION/tarjetas.txt', 'r') as archivo:
    # Lee las líneas del archivo
    lineas = archivo.readlines()

# Verifica que haya al menos dos tarjetas para realizar los métodos
if len(lineas) < 2:
    print("Se necesitan al menos dos tarjetas para realizar los métodos.")
else:
    tarjetas = [line.strip() for line in lineas]

    # Realiza los métodos y almacena los resultados en un diccionario por método
    resultados = {
        "Metodo Basico": [metodo_basico(tarjeta) for tarjeta in tarjetas],
        "Metodo Similitud": [metodo_similitud(tarjetas[0], tarjeta) for tarjeta in tarjetas[1:]],
        "Metodo Activacion": [metodo_activacion(tarjeta) for tarjeta in tarjetas],
        "Metodo Identacion Logica": [metodo_identacion_logica(tarjeta) for tarjeta in tarjetas],
        "Metodo Sofia": [metodo_sofia(tarjetas[0], tarjeta) for tarjeta in tarjetas[1:]]
    }

    # Guarda los resultados en archivos de texto separados por método
    for metodo, resultados_metodo in resultados.items():
        nombre_archivo = f"{metodo}.txt"
        with open(nombre_archivo, 'w') as resultado_archivo:
            for resultado in resultados_metodo:
                resultado_archivo.write(resultado + '\n')

    # Imprime los resultados
    for metodo, resultados_metodo in resultados.items():
        print(f"Resultados del {metodo}:")
        for resultado in resultados_metodo:
            print(resultado)
