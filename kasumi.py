from libs.console import Console
from libs.interface import ConsoleUtils

terminal = Console()


if __name__ == "__main__":
    while True:
        ret = terminal.exec(ConsoleUtils.getcmd_by_line())
        if ret == Console.SIGNAL_EXIT:
            break
        if ret == Console.SIGNAL_FAILED:
            ConsoleUtils.command_failed()
