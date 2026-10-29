from logstats import count_levels, top_errors, format_report


def main():
    filename = input("Введите имя файла: ").strip()

    # Первый проход: подсчёт уровней.
    with open(filename, encoding="utf-8") as log:
        counts = count_levels(log)

    # Второй проход: поиск частых ошибок.
    with open(filename, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    total = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total)
    print(error_count)
    print(broken_count)

    report_text = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as report:
        report.write(report_text)


if __name__ == "__main__":
    main()
