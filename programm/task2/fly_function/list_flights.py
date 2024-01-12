#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list_flights(flights):
    """
    Функция для вывода списка рейсов на экран.
    Выводит табличное представление списка рейсов,
    включая номер, название пункта назначения,
    номер рейса и тип самолета.
    """
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

    for idx, flight in enumerate(flights, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
                flight.get('destination', ''),
                flight.get('flight number', ''),
                flight.get('type of plane', 0)
            )
        )
    print(line)
