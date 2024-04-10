import sys


def txt_importer(path_file):
    try:
        splitted = path_file.split(".")
        if splitted[len(splitted) - 1] != "txt":
            print("Formato inválido", file=sys.stderr)

        with open(path_file) as file:
            return file.read().splitlines()

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
