# Proxy_Scraper
Get any type of proxies in 1 click!

version: 1.0

author: Zelow#9999

## Download

`https://pypi.org/project/proxy_scraper`

You can download the `proxy_scraper` module with Python Package Index (PyPI).

### Download with pip:

`$ pip install proxy_scraper`

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

## Exemples
![image](https://cdn.discordapp.com/attachments/890172654605180938/890305570010202132/unknown.png)

![image](https://cdn.discordapp.com/attachments/890172654605180938/890305570165379112/unknown-1.png)

![image](https://cdn.discordapp.com/attachments/890172654605180938/890305570324750406/unknown-2.png) 
