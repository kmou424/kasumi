def remove_prefix(s: str, prefix: str):
    if s.startswith(prefix):
        s = s[len(prefix):]
    return s


def remove_suffix(s: str, suffix: str):
    if s.endswith(suffix):
        s = s[:len(s) - len(suffix)]
    return s


def remove_all(s: str, rm: str):
    s = replace_all(s, rm, '')
    return s


def replace_all(s: str, o: str, rp):
    while o in s:
        s = s.replace(o, rp)
    return s


def substr(s: str, start, length):
    if len(s) <= start:
        return ""
    if len(s) < start + length:
        return ""
    return s[start:start + length]
