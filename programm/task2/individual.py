#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fly_function import add_flight, list_flights, find_flights

if __name__ == '__main__':
    flights = []

    print(">>> Выберите нужную команду: add, list, find или exit ")

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            add_flight.add_flight(flights)

        elif command == 'list':
            list_flights.list_flights(flights)

        elif command == 'find':
            find_flights.find_flights(flights)
