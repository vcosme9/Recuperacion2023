# Ejercicio 1
print('########### Ejercicio 1 ########### ')

def mediana(diccionario):
    valores = list(diccionario.values())

    longitud = len(valores)
    indice_central = longitud // 2

    if longitud % 2 == 1:
        mediana = valores[indice_central]
    else:
        mediana = (valores[indice_central] + valores[indice_central - 1]) / 2

    return mediana

diccionario = {'valor0': 5, 'valor1': 3, 'valor2': 8}
res = mediana(diccionario)
print(f"La mediana es: {res}")

print("-----------------------------------------------------")

# Ejercicio 2
print('########### Ejercicio 2 ########### ')

import csv
def procesar(archivo_csv, numero_curso):
    estudiantes = []

    with open(archivo_csv, 'r') as archivo:
        reader = csv.reader(archivo)
        next(reader)  # Saltar la primera línea (encabezados)

        for linea in reader:
            if linea[3] == str(numero_curso):
                estudiantes.append((linea[0], linea[1], linea[2], linea[3]))
        if len(estudiantes) == 0:
            raise ValueError ("No hay ningun alumno en ese curso")
    return estudiantes

estudiantes = procesar('alumnos.csv', 3)
print(estudiantes)

print("-----------------------------------------------------")

# Ejercicio 3
print('########### Ejercicio 3 ########### ')

def combinar(dic1, dic2, dic3):
    dic_final = {}
    for nombre in dic1:
        dic_final[nombre] = {
            'edad': dic1[nombre],
            'profesion': dic2[nombre],
            'sueldo': dic3[nombre]
        }
        #print(dic_final)
    return dic_final

diccionario_nombre_edades = {'Ana':25, 'Juan': 30, 'Maria':28}
diccionario_nombres_profesiones = {'Ana': 'Ingeniera', 'Juan': 'Doctor', 'Maria': 'Abogada'}
diccionario_nombres_sueldos = {'Ana': 5000, 'Juan': 7000, 'Maria': 6000}
diccionario_final = combinar(diccionario_nombre_edades, diccionario_nombres_profesiones, diccionario_nombres_sueldos)
print(diccionario_final)

print("-----------------------------------------------------")

# Ejercicio 4
print('########### Ejercicio 4 ########### ')

def palabra_repetida(archivo_txt):
    contador_palabras = {}

    with open(archivo_txt, 'r') as archivo:
        for linea in archivo:
            palabras = linea.split()

            for palabra in palabras:
                if palabra in contador_palabras:
                    contador_palabras[palabra] += 1
                else:
                    contador_palabras[palabra] = 1
        #print(contador_palabras)

    palabra_mas_repetida = max(contador_palabras, key=contador_palabras.get)
    return palabra_mas_repetida

archivo = 'palabras.txt'
palabra = palabra_repetida(archivo)
print(f"Palabra más repetida: {palabra}")
print("-----------------------------------------------------")