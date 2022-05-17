from pathlib import Path

from apis.console_utils import parse_command
from apis.path_utils import build_path
from apis.string_utils import remove_prefix, remove_suffix
from config import LANGUAGE
from libs.consts import MODULE_PATHS
from libs.imports import import_mod, set_module_path


class Console:
    CONSOLE_MODULES = {}

    SIGNAL_Y = 0
    SIGNAL_N = 1
    SIGNAL_EXIT = 2
    SIGNAL_CONTINUE = 3

    SIGNAL_FAILED = -1

    _EXIT_CMD_LIST = ['q', 'exit', 'quit']

    def exec(self, cmd: str) -> int:
        # Clean up command
        while cmd.startswith(' '):
            cmd = remove_prefix(cmd, ' ')
        while cmd.endswith(' '):
            cmd = remove_suffix(cmd, ' ')
        # Parse command in to argv list
        argv = parse_command(cmd)
        if argv is None:
            print("Syntax error")
            return Console.SIGNAL_FAILED
        if len(argv) < 1:
            return Console.SIGNAL_CONTINUE

        prog = argv[0]
        # If exit
        if prog in Console._EXIT_CMD_LIST:
            return Console.SIGNAL_EXIT

        found_prog = False
        # Check command module
        for i in MODULE_PATHS:
            package_path = Path(build_path([i, 'modules', 'bin', prog]))
            package_init_path = Path(build_path([i, 'modules', 'bin', prog]) + '__init__' + '.py')
            if package_path.exists() and package_path.is_dir() and \
                    package_init_path.exists() and package_init_path.is_file():
                found_prog = True
                set_module_path(i)
                break

        if not found_prog:
            print("{cmd}: Command not found".format(cmd=prog))
            return Console.SIGNAL_FAILED

        if prog not in self.CONSOLE_MODULES:
            args = {
                'lang': LANGUAGE
            }
            self.CONSOLE_MODULES[prog] = import_mod(prog).Module(args=args)
        ret = self.CONSOLE_MODULES[prog].exec(argv)
        if ret != 0:
            return self.SIGNAL_FAILED
        return Console.SIGNAL_CONTINUE
