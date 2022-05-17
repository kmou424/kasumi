import hashlib
import os
import shutil
import stat
import sys
from urllib.parse import urlparse

import requests

from libs.consts import SYSTEM_TYPE


def _flush_stdout():
    sys.stdout.flush()


class ArgsError:
    @staticmethod
    def args_num_error(cmd: str):
        sys.stdout.write("{cmd}: Too many/few argument(s), please recheck your command!\n".format(cmd=cmd))
        _flush_stdout()

    @staticmethod
    def args_type_error(cmd: str):
        sys.stdout.write("{cmd}: Wrong argument(s), please recheck your command!\n".format(cmd=cmd))
        _flush_stdout()

    @staticmethod
    def args_id_out_of_bounds_error(cmd: str, ids: str):
        sys.stdout.write("{cmd}: ID {id} out of bounds, please recheck your command!\n".format(cmd=cmd, id=ids))
        _flush_stdout()


class ConsoleUtils:
    Y_CMD_LIST = ['Y', 'y', 'yes']
    N_CMD_LIST = ['N', 'n', 'no']

    @staticmethod
    def pause():
        print()
        print("Press any key to continue...")
        input()

    @staticmethod
    def clear():
        if SYSTEM_TYPE == "Windows":
            os.system("CLS")
        elif SYSTEM_TYPE == "Linux":
            os.system("clear")

    @staticmethod
    def is_user_accept():
        ipt = str(input())
        if ipt in ConsoleUtils.Y_CMD_LIST:
            return True
        elif ipt in ConsoleUtils.N_CMD_LIST:
            return False
        else:
            return None

    @staticmethod
    def command_failed():
        sys.stdout.write(' × ')
        sys.stdout.flush()

    @staticmethod
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

    @staticmethod
    def getcmd_by_line(has_header=True) -> str:
        if has_header:
            print("\033[31m♡kasumi♡ \033[37m=> ", end="")
            sys.stdout.flush()
        return sys.stdin.readline().replace("\n", "")


class FileUtils:
    @staticmethod
    def rmtree(path: str):
        if 'linux' in sys.platform or 'mac' in sys.platform:
            os.system('rm -rf {path}'.format(path=path))
        else:
            return shutil.rmtree(path, onerror=FileUtils.__onRmtreeError)

    @staticmethod
    def __onRmtreeError(func, path, execinfo):
        os.chmod(path, stat.S_IWRITE)
        func(path)


class RequestUtils:
    @staticmethod
    def build_proxies(proxy_addr: str):
        if proxy_addr is None:
            return None
        return {
            'http': proxy_addr,
            'https': proxy_addr
        }

    @staticmethod
    def get_content_from_url(url: str, proxies=None, headers=None):
        response = requests.get(url, proxies=proxies, headers=headers)
        return {
            'content': response.content,
            'status_code': response.status_code
        }


class PathUtils:
    @staticmethod
    def build_path(paths: list):
        path = ""
        for i in paths:
            path += PathUtils.format_path(i)
        return path

    @staticmethod
    def format_path(path: str):
        if SYSTEM_TYPE == "Windows":
            replace_delimiter = "/"
            path_delimiter = "\\"
        else:
            replace_delimiter = "\\"
            path_delimiter = "/"
        while replace_delimiter in path:
            path = path.replace(replace_delimiter, path_delimiter)
        if not path.endswith(path_delimiter):
            path = path + path_delimiter
        return path


class StringUtils:
    @staticmethod
    def remove_prefix(s: str, prefix: str):
        if s.startswith(prefix):
            s = s[len(prefix):]
        return s

    @staticmethod
    def remove_suffix(s: str, suffix: str):
        if s.endswith(suffix):
            s = s[:len(s) - len(suffix)]
        return s

    @staticmethod
    def remove_all(s: str, rm: str):
        s = StringUtils.replace_all(s, rm, '')
        return s

    @staticmethod
    def replace_all(s: str, o: str, rp):
        while o in s:
            s = s.replace(o, rp)
        return s

    @staticmethod
    def substr(s: str, start, length):
        if len(s) <= start:
            return ""
        if len(s) < start + length:
            return ""
        return s[start:start + length]


class URLUtils:
    __args: dict
    __hostname: str
    __baseurl: str

    def __init__(self, url: str):
        self.__hostname = url[:url.find("://")] + "://" + urlparse(url).hostname
        self.__baseurl = url[:url.rfind('/') + 1]
        url = url.replace(self.__baseurl, '')
        if url.startswith('/'):
            url = url[1:]
        if url.startswith('?'):
            url = url[1:]
        self.__args = {}
        if url == '':
            return
        args_list = url.split('&')
        args_lists = []
        for i in range(len(args_list)):
            # First equal symbol
            feq = args_list[i].find('=')
            tmp = []
            if feq != -1:
                tmp.append(args_list[i][:feq])
                tmp.append(args_list[i][feq + 1:])
            else:
                tmp.append(args_list[i])
            args_lists.append(tmp)
        for i in args_lists:
            if len(i) == 2:
                self.__args[i[0]] = i[1]
            else:
                self.__args[i[0]] = None

    def add_arg(self, key: str, value: str):
        if self.has_arg(key):
            return
        self.__args[key] = value

    def build_url(self):
        url = self.__baseurl
        if url.endswith('/'):
            url = url[:-1]
        is_first = False
        for i in self.__args:
            arg = ""
            if not is_first:
                arg += '?'
                is_first = True
            else:
                arg += '&'
            if self.__args[i] is None:
                arg += i
            else:
                arg += i + "=" + self.__args[i]
            url += arg
        return url

    def get_arg(self, key: str):
        return self.__args[key]

    def get_hostname(self):
        ret = self.__hostname
        if ret.endswith('/'):
            ret = ret[:-1]
        return ret

    def get_baseurl(self):
        return self.__baseurl

    def has_arg(self, key: str) -> bool:
        return key in self.__args

    def set_arg(self, key: str, value: str):
        if not self.has_arg(key):
            return
        self.__args[key] = value
