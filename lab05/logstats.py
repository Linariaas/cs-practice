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

def top_errors(lines, n: int) -> list:
    """Возвращает n самых частых сообщений уровня ERROR."""
    error_counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] == "ERROR":
            message = event["message"]
            error_counts[message] = (
                error_counts.get(message, 0) + 1
            )

    sorted_errors = sorted(
        error_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )

    return [
        [message, count]
        for message, count in sorted_errors[:n]
    ]

def format_report(counts: dict, errors: list) -> str:
    """Формирует текстовый отчёт по журналу."""
    lines = [
        "Отчёт по журналу",
        "",
    ]

    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")

    lines.append("")
    lines.append("Частые ошибки:")

    for message, count in errors:
        lines.append(f"- {message} — {count}")

    return "\n".join(lines) + "\n"
