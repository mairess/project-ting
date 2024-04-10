from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def search(self, index):
        if 0 <= index < len(self.data) and isinstance(index, int):
            return self.data[index]

        raise IndexError("Índice Inválido ou Inexistente")

    def __repr__(self):
        str_items = ""
        for index in range(len(self.data)):
            str_items += str(self.data[index])
            if index + 1 < len(self.data):
                str_items += ", "
        return "Queue(" + str_items + ")"
