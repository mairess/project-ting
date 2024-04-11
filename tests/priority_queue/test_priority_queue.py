from ting_file_management.priority_queue import PriorityQueue
import pytest

text_file_4_lines = [
    "Acima de tudo,",
    "é fundamental ressaltar que a adoção de",
    "políticas descentralizadoras nos obriga",
    "à análise do levantamento das variáveis envolvidas.",
]

dict_one = {
    "nome_do_arquivo": "arquivo_4_lines.txt",
    "qtd_linhas": 4,
    "linhas_do_arquivo": text_file_4_lines,
}


text_file_6_lines = [
    "Acima de tudo,",
    "é fundamental ressaltar que a adoção de",
    "políticas descentralizadoras nos obriga",
    "à análise do levantamento das variáveis envolvidas.",
    "à análise do levantamento das variáveis envolvidas.",
    "à análise do levantamento das variáveis envolvidas.",
]

dict_two = {
    "nome_do_arquivo": "arquivo_6_lines.txt",
    "qtd_linhas": 6,
    "linhas_do_arquivo": text_file_6_lines,
}


text_file_3_lines = [
    "Acima de tudo,",
    "é fundamental ressaltar que a adoção de",
    "políticas descentralizadoras nos obriga",
]

dict_three = {
    "nome_do_arquivo": "arquivo_3_lines.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": text_file_3_lines,
}


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue(dict_one)
    queue.enqueue(dict_two)
    queue.enqueue(dict_three)
    assert queue.high_priority.__len__() == 2
    assert queue.regular_priority.__len__() == 1
    assert queue.search(1)["nome_do_arquivo"] == "arquivo_3_lines.txt"

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(999)

    queue.dequeue()
    assert queue.high_priority.__len__() == 1
