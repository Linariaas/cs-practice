def parse_record(line: str) -> dict:
    """Разбирает строку формата город;температура;дата."""

    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("В записи должно быть три поля")

    city = parts[0].strip()
    temp_text = parts[1].strip()
    date = parts[2].strip()

    if not city:
        raise ValueError("Не указан город")

    if not date:
        raise ValueError("Не указана дата")

    try:
        temperature = float(temp_text.replace(",", "."))
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {
        "city": city,
        "temperature": temperature,
        "date": date
    }


def read_valid(lines: list[str]) -> list[dict]:
    """Возвращает корректные записи, пропуская пустые и ошибочные строки."""

    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            record = parse_record(line)
        except ValueError:
            continue

        records.append(record)

    return records


def average_by_city(records: list[dict]) -> dict:
    """Считает среднюю температуру каждого города с округлением до десятых."""

    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        totals[city] = totals.get(city, 0.0) + temperature
        counts[city] = counts.get(city, 0) + 1

    averages = {}

    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    """Возвращает город с самой высокой средней температурой.
    При равенстве выбирает первый по алфавиту.
    """

    averages = average_by_city(records)

    if not averages:
        return ""

    return min(averages, key=lambda city: (-averages[city], city))