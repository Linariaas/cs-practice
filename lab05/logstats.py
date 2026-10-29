def parse_event(line: str) -> dict:
    """Разбирает строку журнала на время, уровень и сообщение."""
    line = line.strip()

    if not line:
        raise ValueError("Пустая строка")

    parts = line.split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError(f"Некорректная строка: {line}")

    time_str, level, message = parts

    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}

    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень: {level}")

    return {
        "time": time_str,
        "level": level,
        "message": message,
    }

def count_levels(lines) -> dict:
    """Считает количество записей каждого уровня."""
    counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"

        counts[level] = counts.get(level, 0) + 1

    return counts

