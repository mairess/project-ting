from ting_file_management.priority_queue import PriorityQueue
import pytest

from tests.priority_queue.mocks import dict_one
from tests.priority_queue.mocks import dict_two
from tests.priority_queue.mocks import dict_three


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
