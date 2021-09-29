# Proxy_Scraper
Get any type of proxies in 1 click!

version: 1.3

author: github.com/zeloww

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPi version](https://badgen.net/pypi/v/pip/)](https://pypi.com/project/pip)
[![PyPi license](https://img.shields.io/pypi/l/fpvgcc.svg?color=blue)](https://pypi.com/project/pip/)
![PyPi download](https://pepy.tech/badge/proxy_scraper)

## Download

You can download the `https://PyPi.org/project/proxy_scraper` module with Python Package Index (PyPI).

### Download with pip:

`$ pip install proxy_scraper`

## Examples

### getproxy()

```py
from proxy_scraper import getproxy
print(getproxy(type="https", timeout=10)

>>> 88.198.24.108:1080
```

### getproxies()

```py
from proxy_scraper import getproxies
print(getproxies(type="http", number=2)

>>> ['104.255.170.91:51676', '88.198.24.108:1080']
```

### proxies_checker()

```py
from proxy_scraper import proxies_checker
print(proxies_checker(url="https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100")

>>> {
        'file: None': [],
        'url: https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=5': [
            '217.149.135.21:5678',
            '54.38.163.25:5678',
            '185.216.163.133:1080',
            '185.161.245.1:1080',
            '179.49.117.166:5678',
        ]
     }
```

## Documentation

The module using the API of proxyscrape: `https://docs.proyscrape.com`

### getproxies()

#### return random proxies with settings

`type`: **Type** -> `string`, **Default** -> `'all'` Choice the type of proxies (http, https, socks4...)

`country`: **Type** -> `string`, **Default** -> `'all'` Choice the country of proxies (fr, us...)

`timeout` **Type** -> `int`, **Default** -> `1500` Choice the timeout of proxies (in seconds)

`checker`: **Type** -> `boolean`, **Default** -> `False` Check the proxies (if you don't use the default api)

`request_url` **Type** -> `string`, **Default** -> `'https://google.com'` Choice the website to try if the proxy work with `checker()`

`number`: **Type** -> `boolean`, **Default** -> `None` Get a special numbers of proxies

`auth`: **Type** -> `string`, **Default** -> `None` If you have a auth key for the api of croxyproxy (not mandatory)

`download`: **Type** -> `boolean`, **Default** -> `False` Download a file of the proxies

`ssl` **Type** -> `boolean`, **Default** -> `True` Choice if you want SSL for your proxies

`anonymity` **Type** -> `string`, **Default** -> `'all'`Choice the anonimity of your proxies

`format` **Type** -> `string`, **Default** -> `'normal'` Choice the format of your proxies (normal, json)

`dict`  **Type** -> `boolean`, **Default** -> `False` Choice if you want a dict for your proxies

`url` **Type** -> `string`, **Default** -> `None` Choice a special url for the lists of proxies

### getproxy()

#### return a random proxy with settings

`type`: **Type** -> `string`, **Default** -> `'all'` Choice the type of proxies (http, https, socks4...)

`country`: **Type** -> `string`, **Default** -> `'all'` Choice the country of proxies (fr, us...)

`timeout` **Type** -> `int`, **Default** -> `1500` Choice the timeout of proxies (in seconds)

`checker`: **Type** -> `boolean`, **Default** -> `False` Check the proxies (if you don't use the default api)

`request_url` **Type** -> `string`, **Default** -> `'https://google.com'` Choice the website to try if the proxy work with `checker()`

`number`: **Type** -> `boolean`, **Default** -> `None` Get a special numbers of proxies for the random.choice

`auth`: **Type** -> `string`, **Default** -> `None` If you have a auth key for the api of croxyproxy (not mandatory)

`download`: **Type** -> `boolean`, **Default** -> `False` Download a file of the proxies

`ssl` **Type** -> `boolean`, **Default** -> `True` Choice if you want SSL for your proxies

`anonymity` **Type** -> `string`, **Default** -> `'all'`Choice the anonimity of your proxies

`format` **Type** -> `string`, **Default** -> `'normal'` Choice the format of your proxies (normal, json)

`dict`  **Type** -> `boolean`, **Default** -> `False` Choice if you want a dict for your proxies

`url` **Type** -> `string`, **Default** -> `None` Choice a special url for the lists of proxies

### proxies_checker()

#### Check proxies with settings

`file` **Type** -> `string`, **Default** -> `None` Choice a file with proxies for check if they works

`url` **Type** -> `string`, **Default** -> `None` Choice an url with proxies for check if they works

`timeout` **Type** -> `int`, **Default** -> `1500` Choice the timeout of proxies (in seconds)

`number`: **Type** -> `boolean`, **Default** -> `None` Choice a number of good proxies for end the checking

`request_url` **Type** -> `string`, **Default** -> `'https://google.com'` Choice the website to try if the proxy work
