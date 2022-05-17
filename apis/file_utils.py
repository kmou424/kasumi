import os
import shutil
import stat
import sys


def rmtree(path: str):
    if 'linux' in sys.platform or 'mac' in sys.platform:
        os.system('rm -rf {path}'.format(path=path))
    else:
        return shutil.rmtree(path, onerror=__onRmtreeError)


def __onRmtreeError(func, path, execinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)
