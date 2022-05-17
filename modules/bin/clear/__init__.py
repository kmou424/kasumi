import os
import platform

from modules.wrapper import ModuleWrapper

SYSTEM_TYPE = platform.system()


class Module(ModuleWrapper):

    def __init__(self, args: dict):
        super().__init__(args)
        self.mod_name = "clear"
        self.mod_args = []
        self.mod_author = "kmou424"
        self.mod_description = "Clear your screen"
        self.mod_version = "1.0"
        self.mod_version_code = 1

    def help(self):
        print("Usage: clear")

    def exec(self, argv: list):
        if len(argv) != 1:
            self.help()
            return -1
        if SYSTEM_TYPE == "Windows":
            os.system("CLS")
        elif SYSTEM_TYPE == "Linux":
            os.system("clear")
        return 0
