import platform
from urllib.parse import urlparse


SYSTEM_TYPE = platform.system()


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
