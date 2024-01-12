#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_flights(flights):
    """
    Функция для поиска рейсов по типу самолета и вывода результатов на экран.
    Запрашивает у пользователя тип самолета,
    затем ищет все рейсы с этим типом и выводит их табличное представление.
    """
    find_type = input("Введите тип самолета для поиска: ")
    found = []

    for flight in flights:
        if flight['type of plane'] == find_type:
            found.append(flight)

    if not found:
        print(f"Рейсов на самолете типа '{find_type}' не найдено.")
    else:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)

        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "No",
                "Пункт назначения",
                "Номер рейса",
                "Тип самолета"
            )
        )

        print(line)

        for idx, found_flight in enumerate(found, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    found_flight.get('destination', ''),
                    found_flight.get('flight number', ''),
                    found_flight.get('type of plane', 0)
                )
            )
        print(line)
