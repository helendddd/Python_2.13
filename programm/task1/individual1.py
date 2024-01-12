#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import greeting_template

if __name__ == "__main__":
    template = "Уважаемый %F% %N%! Вы делаете работу по замыканиям функций."

    greet_function = greeting_template.create_greeting(template)

    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")

    result = greet_function(last_name, first_name)
    print(result)
