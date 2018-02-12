import csv
import random
from collections import defaultdict


def seleccionarGanador(columna):
    numeroGanador = random.randint(0, len(columna) - 1)
    return numeroGanador


with open("Fiesta de Bienvenida GUL-UCA.csv") as csvDataFile:
    listaAsistentes = defaultdict(list)  # Cada valor en cada columna es agregado a una lista

    reader = csv.DictReader(csvDataFile)  # Lee las filas en formato de diccionario
    for fila in reader:  # Lee cada fila almacenada en el reader
        for (columna, valor) in fila.items():  # Recorre cada lista y valor
            listaAsistentes[columna].append(valor)  # Agrega el valor a la lista apropiada

    numeroGanador = seleccionarGanador(listaAsistentes['Nombres y Apellidos'])

    file = open("Ganador.txt", "w")
    file.write(listaAsistentes["Nombres y Apellidos"][numeroGanador] + " " +
               listaAsistentes["Carrera universitaria"][numeroGanador] + " " +
               listaAsistentes["Número telefonico"][numeroGanador])
    file.close()
