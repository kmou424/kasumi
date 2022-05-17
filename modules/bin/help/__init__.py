from pathlib import Path

from modules.imports import import_interface, import_consts, import_mod

interface = import_interface()

PathUtils = interface.PathUtils

consts = import_consts()


class Module:
    mod_name = "help"
    mod_args = []
    mod_description = "Show help for command"

    def __init__(self, args: dict):
        pass

    @staticmethod
    def help():
        print("Usage: help [command]")

    @staticmethod
    def exec(argv: list):
        if len(argv) == 1:
            Module.help()
            return 0
        if len(argv) != 2:
            Module.help()
            return -1
        # Check command module
        prog = argv[0]
        package_path = Path(PathUtils.build_path([consts.PWD, 'modules', 'bin', argv[1]]))
        package_init_path = Path(PathUtils.build_path([consts.PWD, 'modules', 'bin', argv[1]]) + '__init__' + '.py')

        if (not package_path.exists() or not package_path.is_dir()) or \
                (not package_init_path.exists() or not package_init_path.is_file()):
            print("{cmd}: Package is not found".format(cmd=prog))
            return -1
        module = import_mod(argv[1]).Module({})
        print(">> Module Information")
        print("Name: " + module.mod_name)
        print("Sub-arguments: " + ', '.join(module.mod_args))
        print("Description: " + module.mod_description)
        module.help()

        return 0
