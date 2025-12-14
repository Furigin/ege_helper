import ege_help

cmd = input("Введи задание: ")

if hasattr(ege_help, cmd):
    getattr(ege_help, cmd)()
else:
    print("Такого задания нет")
