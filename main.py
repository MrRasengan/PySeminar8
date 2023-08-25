# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

from random import *
import json

# phone_book = {"Дядя Петя": {"phone_numbers": [9998881234, 9997772233], "birth_day": "121276", "email": "mail@mail.ss"}, 
#               "Тетя Песя": {"phone_numbers": [9998881444]}}

phone_book = {}

def save():
    with open("contact.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))
    print("Контакт сохранен")
def load():
    with open("contact.json", "r", encoding="utf-8") as fh:
        phone_book = json.load(fh)
    return phone_book
    

while True:
    command = input("Введите команду: ")
    if command == "/add":
        name = input("Введите имя нового контакта: ")
        number0 = input("Введите 1й номер: ")
        number1 = input("Введите 2й номер: ")
        bith_day = input("Введите ДР: ")
        mail = input("Введите email: ")
        phone_book[name] = {"phone_numbers": [number0, number1], "birth_day": bith_day, "email": mail}
        print("Контакт добавлен")
    elif command == "/all":
        print("Список всех контактов")
        print(phone_book)
    elif command == "/find":
        name = input("Введите имя для поиска: ")
        if name in phone_book:
            print(name, phone_book[name])
    elif command == "/save":
        save()
    elif command == "/load":
        phone_book = load()
        print("Загрузка контактов выполнена успешно")
    