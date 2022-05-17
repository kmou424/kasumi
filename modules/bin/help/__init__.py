import sys
from pathlib import Path

from libs.imports import import_api, import_consts, import_mod, set_module_path
from modules.wrapper import ModuleWrapper

path_utils = import_api('path_utils')

consts = import_consts()


class Module(ModuleWrapper):
    mod_name = "help"
    mod_args = []
    mod_author = "kmou424"
    mod_description = "Show help for command"
    mod_version = "1.0"
    mod_version_code = 1

    def __init__(self, args: dict):
        super().__init__(args)

    def help(self):
        print("Usage: help [command]")

    def exec(self, argv: list):
        if len(argv) == 1:
            self.help()
            return 0
        if len(argv) != 2:
            self.help()
            return -1

        prog = argv[1]
        found_prog = False
        # Check command module
        for i in consts.MODULE_PATHS:
            package_path = Path(path_utils.build_path([i, 'modules', 'bin', prog]))
            package_init_path = Path(path_utils.build_path([i, 'modules', 'bin', prog]) + '__init__' + '.py')
            if package_path.exists() and package_path.is_dir() and \
                    package_init_path.exists() and package_init_path.is_file():
                found_prog = True
                set_module_path(i)
                break

        if not found_prog:
            print("{cmd}: Package not found".format(cmd=prog))
            return -1

        module = import_mod(argv[1]).Module({})
        print(">> Module Information")
        print("Name: " + module.mod_name)
        print("Author: " + module.mod_author)
        print("Sub-arguments: " + ', '.join(module.mod_args))
        print("Description: " + module.mod_description)
        module.help()

        return 0
