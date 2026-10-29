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

def human_size(n_bytes: int) -> str:
    """Преобразует размер в байтах в удобный формат."""
    if n_bytes < 0:
        raise ValueError("Размер не может быть отрицательным")

    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]

    size = float(n_bytes)
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    if unit_index == 0:
        return f"{n_bytes} Б"

    return f"{size:.1f} {units[unit_index]}"
