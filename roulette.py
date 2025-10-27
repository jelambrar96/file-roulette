import argparse
import csv
import random
import os
import sys


def leer_archivo(file_path, remove_header):
    """
    Lee un archivo .txt o .csv y devuelve una lista de cadenas (una por fila).
    """
    if not os.path.exists(file_path):
        print(f"Error: el archivo '{file_path}' no existe.")
        sys.exit(1)

    ext = os.path.splitext(file_path)[1].lower()

    filas = []
    with open(file_path, "r", encoding="utf-8") as f:
        filas = [line.strip() for line in f if line.strip()]

    if remove_header and len(filas) > 0:
        filas = filas[1:]

    return filas



def main():
    parser = argparse.ArgumentParser(description="Aplicación para leer, mezclar y mostrar archivos línea por línea.")
    parser.add_argument("--file", "-f", required=True, help="Ruta del archivo .csv o .txt")
    parser.add_argument("--seed", "-s", type=int, help="Semilla aleatoria (opcional)")
    parser.add_argument("--remove-header", "-r", action="store_true", help="Elimina la primera fila si existe")

    args = parser.parse_args()

    # Leer archivo y elimina las filas vacias
    filas = [ item for item in leer_archivo(args.file, args.remove_header) if item ]

    # Aplicar semilla si se indica
    seed = args.seed if args.seed is not None else random.randint(0, len(filas) - 1)
    if args.seed is None:
        print(f"Usando semilla aleatoria generada: {seed}")
    random.seed(seed)

    # Mezclar la lista
    random.shuffle(filas)

    # Mostrar una fila por enter
    print("\nPresiona ENTER para mostrar una línea (Ctrl+C para salir)\n")
    for i, fila in enumerate(filas, start=1):
        input()
        print(f"{i}: {fila}", end="")
    print()


if __name__ == "__main__":
    main()
