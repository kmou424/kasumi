import os
import sys

from apis.path_utils import build_path

APPLE_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPod touch; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/604.5.6 (KHTML, '
                  'like Gecko) FxiOS/100.0 Mobile/15E148 Safari/605.1.15'
}
CHROME_REQUEST_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47 '
}

USER_DIRECTORY = os.path.expanduser('~')
KASUMI_USER_DIRECTORY = build_path([USER_DIRECTORY, '.kasumi'])

MODULE_PATHS = [sys.path[0], KASUMI_USER_DIRECTORY]
