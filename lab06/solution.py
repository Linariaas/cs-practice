def count_by_extension(paths: list[str]) -> dict[str, int]:
    """Считает количество файлов по расширениям."""
    counts = {}

    for path in paths:
        # Отделяем имя файла от пути к нему.
        filename = path.replace("\\", "/").rsplit("/", 1)[-1]

        # Ищем последнюю точку именно в имени файла.
        dot_index = filename.rfind(".")

        if dot_index == -1 or dot_index == len(filename) - 1:
            ext = ""
        else:
            ext = filename[dot_index + 1:].lower()

        counts[ext] = counts.get(ext, 0) + 1

    return counts

def deepest_path(paths: list[str]) -> str:
    """Возвращает наиболее вложенный путь."""
    if not paths:
        return ""

    return min(paths, key=lambda p: (-p.count("/"), p))
