import random
from urllib import request


def check_proxy(proxy: str, url: str, timeout: int) -> bool:
    proxy_handler = request.ProxyHandler({
        "https": "http://" + proxy,
        "http": "http://" + proxy,
        "socks4": "socks4://" + proxy,
        "socks5": "socks5://" + proxy
    })
    opener = request.build_opener(proxy_handler)
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0  (Windows NT 6.1; Win64; x64)')]
    request.install_opener(opener)
    result = True
    try:
        response = request.urlopen(url, timeout=timeout)
    except:
        result = False
    finally:
        response.close()
        return result


def get_proxies(checker: bool = False,
                limit: int = None,
                auth: str = None,
                download: bool = False,
                type: str = "all",
                country: str = "all",
                timeout: int = 1000,  # In ms
                ssl: bool = True,
                anonymity: str = "all",
                format: str = "normal",
                request_url: str = "https://google.com/"):
    proxies = []

    ssl = "yes" if ssl else "no"
    download = "getproxies" if download else "displayproxies"
    url = f"https://api.proxyscrape.com/?auth={auth}&request={download}&proxytype={type}&timeout={timeout}&ssl={ssl}&anonimity={anonymity}&country={country}&format={format}".replace(
            ",", "&").replace(" ", "")

    http = request.Request(url)
    with request.urlopen(http) as response:
        data = response.read().decode("utf-8")
    response.close()

    for i, proxy in enumerate(data.split("\r\n")):
        if proxy == '':
            continue
        elif limit and limit == i:
            break
        elif not checker:
            proxies.append(proxy)
            continue
        elif check_proxy(proxy, request_url, timeout):
            proxies.append(proxy)

    return proxies


def check_proxies_from_file(file: str,
                            limit: int = None,
                            timeout: int = 1000, # In ms
                            request_url: str = "https://google.com/"):
    proxies = []

    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        f.close()
    except OSError:
        return proxies
    else:
        for i, proxy in enumerate(content.split("\r\n")):
            if proxy == '':
                continue
            elif limit and limit == i:
                break
            elif check_proxy(proxy, request_url, timeout):
                proxies.append(proxy)

    return proxies
