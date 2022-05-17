import platform

SYSTEM_TYPE = platform.system()


def build_path(paths: list):
    path = ""
    for i in paths:
        path += format_path(i)
    return path


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
