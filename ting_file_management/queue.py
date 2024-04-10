from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = list()

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        return self.__data.pop(0)

    def search(self, index):
        if 0 <= index < len(self.__data) and isinstance(index, int):
            return self.__data[index]

        raise IndexError("Índice Inválido ou Inexistente")

    def __repr__(self):
        str_items = ""
        for index in range(len(self.__data)):
            str_items += str(self.__data[index])
            if index + 1 < len(self.__data):
                str_items += ", "
        return "Queue(" + str_items + ")"
