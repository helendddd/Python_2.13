#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def create_greeting(template):
    """
    Создает функцию для формирования приветственного сообщения.
    """
    def greet(last_name, first_name):
        """
        Формирует приветственное сообщение.
        """
        return template.replace("%F%", last_name).replace("%N%", first_name)

    return greet
