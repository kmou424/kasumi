import hashlib
import os
import sys

from libs.consts import SYSTEM_TYPE

Y_CMD_LIST = ['Y', 'y', 'yes']
N_CMD_LIST = ['N', 'n', 'no']


def pause():
    print()
    print("Press any key to continue...")
    input()


def clear():
    if SYSTEM_TYPE == "Windows":
        os.system("CLS")
    elif SYSTEM_TYPE == "Linux":
        os.system("clear")


def is_user_accept():
    ipt = str(input())
    if ipt in Y_CMD_LIST:
        return True
    elif ipt in N_CMD_LIST:
        return False
    else:
        return None


def command_failed():
    sys.stdout.write(' \033[31m×\033[31m ')
    sys.stdout.flush()


def parse_command(command: str):
    plist = []
    rp_list = {}
    for i in range(len(command)):
        if command[i] == '\"':
            plist.append(i)
    if len(plist) % 2 == 1:
        return None
    for i in range(len(plist)):
        if i % 2 == 1:
            continue
        arg = command[plist[i]:plist[i + 1] + 1]
        sha1_of_arg = hashlib.sha1(arg.encode(encoding='utf-8')).hexdigest()
        command = command.replace(arg, sha1_of_arg)
        rp_list[sha1_of_arg] = arg[1:-1]
    cmd_list = command.split(' ')
    for i in rp_list:
        idx = cmd_list.index(i)
        cmd_list[idx] = rp_list[i]
    return cmd_list


def getcmd_by_line(has_header=True) -> str:
    if has_header:
        print("\033[31m♡kasumi♡ \033[37m=> ", end="")
        sys.stdout.flush()
    return sys.stdin.readline().replace("\n", "")
