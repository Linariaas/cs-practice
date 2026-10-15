def parse_record(line: str) -> dict:
    """
    Разбирает строку "город;температура;дата" в словарь.
    Если строка негодная — возбуждает ValueError.
    """
    # Режем строку по точке с запятой
    parts = line.split(";")

    # Проверяем: должно быть ровно 3 части
    if len(parts) != 3:
        raise ValueError(f"не ровно три поля: {line!r}")

    # Достаём три части и убираем лишние пробелы по краям
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()

    # Город не должен быть пустым
    if not city:
        raise ValueError(f"город пустой: {line!r}")

    # Дата не должна быть пустой
    if not date:
        raise ValueError(f"дата пустая: {line!r}")

    # Пытаемся превратить температуру в число
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"температура не число: {temp_str!r}")

    # Возвращаем словарик
    return {"city": city, "temp": temp, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    """
    Разбирает строки журнала, пропуская пустые и негодные.
    Возвращает список словарей (только хорошие записи).
    """
    records = []  # сюда складываем хорошие записи

    for line in lines:
        # Если строка пустая (или только пробелы) — пропускаем молча
        if not line.strip():
            continue

        # Пытаемся разобрать строку
        try:
            record = parse_record(line)
            records.append(record)  # получилось — добавляем
        except ValueError:
            pass  # не получилось — пропускаем, не падаем

    return records


def average_by_city(records: list[dict]) -> dict:
    """
    Считает среднюю температуру по каждому городу.
    Округляет до десятых (1 знак после точки).
    Возвращает словарь {город: средняя_температура}.
    """
    total = {}   # сумма температур по городам
    count = {}   # количество записей по городам

    for record in records:
        city = record["city"]
        temp = record["temp"]

        # Прибавляем температуру к сумме
        total[city] = total.get(city, 0) + temp
        # Увеличиваем счётчик записей
        count[city] = count.get(city, 0) + 1

    # Считаем среднее для каждого города
    result = {}
    for city in total:
        result[city] = round(total[city] / count[city], 1)

    return result


def warmest_city(records: list[dict]) -> str:
    """
    Находит город с наибольшей средней температурой.
    Если несколько городов с одинаковой температурой —
    возвращает первый по алфавиту.
    """
    # Сначала считаем средние по всем городам
    averages = average_by_city(records)

    # Находим максимальную температуру
    max_temp = max(averages.values())

    # Собираем все города с этой максимальной температурой
    candidates = []
    for city, temp in averages.items():
        if temp == max_temp:
            candidates.append(city)

    # Возвращаем первый по алфавиту
    return min(candidates)
