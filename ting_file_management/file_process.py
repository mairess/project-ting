import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer

my_queue = Queue()


def process(path_file, instance: Queue):
    if txt_importer(path_file) is None:
        return None

    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    if not any(d["nome_do_arquivo"] == path_file for d in instance.data):
        print(dict, file=sys.stdout)
        instance.enqueue(dict)


def remove(instance: Queue):
    if instance.__len__() == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        file_removed = instance.data[0]["nome_do_arquivo"]
        instance.dequeue()
        print(f"Arquivo {file_removed} removido com sucesso", file=sys.stdout)


def file_metadata(instance: Queue, position):
    if position < 0 or position >= instance.__len__():
        print("Posição inválida", file=sys.stderr)
    else:
        print(instance.search(position), file=sys.stdout)
