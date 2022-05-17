import os

from modules.imports import import_consts

SYSTEM_TYPE = import_consts().SYSTEM_TYPE


class Module:
    mod_name = "clear"
    mod_args = []
    mod_description = "Clear your screen"

    def __init__(self, args: dict):
        pass

    @staticmethod
    def help():
        print("Usage: clear")

    @staticmethod
    def exec(argv: list):
        if len(argv) != 1:
            Module.help()
            return -1
        if SYSTEM_TYPE == "Windows":
            os.system("CLS")
        elif SYSTEM_TYPE == "Linux":
            os.system("clear")
        return 0
