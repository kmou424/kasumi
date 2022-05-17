import requests


def build_proxies(proxy_addr: str):
    if proxy_addr is None:
        return None
    return {
        'http': proxy_addr,
        'https': proxy_addr
    }


def get_content_from_url(url: str, proxies=None, headers=None):
    response = requests.get(url, proxies=proxies, headers=headers)
    return {
        'content': response.content,
        'status_code': response.status_code
    }
