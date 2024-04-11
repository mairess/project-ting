from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue) -> list[dict] | list:
    data, result = instance.data, []

    for dic in data:
        ocorrencias, palavra, arquivo = [], word, dic["nome_do_arquivo"]

        for index, value in enumerate(dic["linhas_do_arquivo"]):
            if word.lower() in value.lower():
                ocorrencias.append({"linha": index + 1})

        if ocorrencias:
            result.append(
                {
                    "palavra": palavra,
                    "arquivo": arquivo,
                    "ocorrencias": ocorrencias,
                }
            )
    return result


def search_by_word(word: str, instance: Queue) -> list[dict] | list:
    data, result = instance.data, []

    for dic in data:
        ocorrencias, palavra, arquivo = [], word, dic["nome_do_arquivo"]

        for index, line_value in enumerate(dic["linhas_do_arquivo"]):
            if word.lower() in line_value.lower():
                ocorrencias.append(
                    {"linha": index + 1, "conteudo": line_value}
                )

        if ocorrencias:
            result.append(
                {
                    "palavra": palavra,
                    "arquivo": arquivo,
                    "ocorrencias": ocorrencias,
                }
            )
    return result
