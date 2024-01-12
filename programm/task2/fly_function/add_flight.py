#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add_flight(flights):
    """
    Функция для добавления нового рейса в список.
    Запрашивает у пользователя название пункта назначения,
    номер рейса и тип самолета,
    создает новый рейс и добавляет его в общий список рейсов,
    сортируя по названию пункта назначения.
    """
    destination = input("Введите название пункта назначения: ")
    flight_number = input("Введите номер рейса: ")
    plane_type = input("Введите тип самолета: ")

    new_flight = {
        'destination': destination,
        'flight number': flight_number,
        'type of plane': plane_type
    }

    flights.append(new_flight)
    flights.sort(key=lambda x: x['destination'])
