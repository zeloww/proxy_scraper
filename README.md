# Proxy_Scraper

Get any type of proxies easier !

version: 1.8

[![PyPi license](https://img.shields.io/pypi/l/fpvgcc.svg?color=blue)](https://pypi.com/project/pip/)
![PyPi download](https://pepy.tech/badge/proxy_scraper)

## Download using PyPI

You can download the module [here](https://pypi.org/project/proxy_scraper).

## Download using pip:

```bash
~$ python3 -m pip install proxy_scraper
```

## Examples

```py
from proxy_scraper import get_proxies
# Creates a lambda function to return randomly only one proxy.
# WARN : they are not checked !
get_proxy = lambda t, d: __import__("random").choice(get_proxies(type=t, timeout=d))
print(get_proxy("https", 10)

>>> 88.198.24.108:1080
```

```py
from proxy_scraper import get_proxies
# Returns a list of checked proxies.
print(get_proxies(checked=True, type="http", number=2)

>>> ['104.255.170.91:51676', '88.198.24.108:1080']
```

```py
from proxy_scraper import check_proxies_from_file
# Checks proxies from the specified path. If not found, it returns an empty list.
print(check_proxies_from_file("proxies.txt", timeout=100))

>>> ['217.149.135.21:5678', '54.38.163.25:5678', '185.216.163.133:1080', '185.161.245.1:1080', '179.49.117.166:5678']
```

## Documentation

The module uses the [ProxyScrape's API](https://docs.proxy_scrape.com).
