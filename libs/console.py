from pathlib import Path

from config import LANGUAGE
from libs.consts import PWD
from libs.interface import StringUtils, ConsoleUtils, PathUtils
from modules.imports import import_mod


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
            cmd = StringUtils.remove_prefix(cmd, ' ')
        while cmd.endswith(' '):
            cmd = StringUtils.remove_suffix(cmd, ' ')
        # Parse command in to argv list
        argv = ConsoleUtils.parse_command(cmd)
        if argv is None:
            print("Syntax error")
            return Console.SIGNAL_FAILED
        if len(argv) < 1:
            return Console.SIGNAL_CONTINUE

        prog = argv[0]
        # If exit
        if prog in Console._EXIT_CMD_LIST:
            return Console.SIGNAL_EXIT

        # Check command module
        package_path = Path(PathUtils.build_path([PWD, 'modules', 'bin', prog]))
        package_init_path = Path(PathUtils.build_path([PWD, 'modules', 'bin', prog]) + '__init__' + '.py')

        if (not package_path.exists() or not package_path.is_dir()) or \
                (not package_init_path.exists() or not package_init_path.is_file()):
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
        # # command: add
        # if exec_prog == 'add':
        #     self.dl_list = CommandHelper.add(cmd_list, self.dl_list)
        # # command: attrs
        # elif exec_prog == 'attrs':
        #     CommandHelper.attrs(cmd_list)
        # # command: clear
        # elif exec_prog == 'clear':
        #     ConsoleHelper.clear()
        # # command: delete
        # elif exec_prog == 'delete':
        #     self.dl_list = CommandHelper.delete(cmd_list, self.dl_list)
        # # command: down
        # elif exec_prog == 'down':
        #     self.dl_list = CommandHelper.down(cmd_list, self.dl_list)
        # # command: list
        # elif exec_prog == 'list':
        #     CommandHelper.list(cmd_list, self.dl_list)
        # # command: set
        # elif exec_prog == 'set':
        #     self.dl_list = CommandHelper.set(cmd_list, self.dl_list)
        # # command: star
        # elif exec_prog == 'star':
        #     self.dl_list = CommandHelper.star(cmd_list, self.dl_list)
        # # command: help
        # elif exec_prog == 'help':
        #     ConsoleHelper.print_console_help(cmd_list)
        return Console.SIGNAL_CONTINUE
