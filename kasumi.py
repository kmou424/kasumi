from apis.console_utils import getcmd_by_line, command_failed
from libs.console import Console

terminal = Console()


if __name__ == "__main__":
    while True:
        ret = terminal.exec(getcmd_by_line())
        if ret == Console.SIGNAL_EXIT:
            break
        if ret == Console.SIGNAL_FAILED:
            command_failed()
