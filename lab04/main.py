import sys
from stats import average_by_city, read_valid, warmest_city

# 1. Читаем всё, что подали на вход (из файла или с клавиатуры)
lines = sys.stdin.read().splitlines()

# 2. Считаем, сколько строк НЕ пустые
#    (пустые строки — это не ошибки, их просто игнорируем)
non_empty_count = 0
for line in lines:
    if line.strip():          # если в строке есть хоть что-то кроме пробелов
        non_empty_count += 1

# 3. Отбираем только хорошие (валидные) записи
records = read_valid(lines)

# 4. Считаем количество ошибок:
#    ошибки = (непустые строки) - (хорошие записи)
errors = non_empty_count - len(records)

# 5. Печатаем отчёт — три строки

# Первая строка: сколько записей разобрано
print(len(records))

# Вторая строка: сколько строк пропущено из-за ошибок
print(errors)

# Третья строка: средняя температура самого тёплого города
# (только если есть хоть какие-то данные)
if records:
    best = warmest_city(records)       # находим самый тёплый город
    avgs = average_by_city(records)    # считаем средние по всем городам
    print(f"{avgs[best]:.1f}")         # печатаем с 1 знаком после точки
