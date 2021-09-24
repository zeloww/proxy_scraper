from urllib import request
from random import choice

class proxies:
    proxies_list = []

    def getproxies(dict:bool=False, checker:bool=False, number:int=None, auth:str=None, download:bool=False, type:str="all", country:str="all", timeout:int=1500, ssl:bool=True, anonymity:str="all", format:str="normal", url:str=None, request_url:str="https://google.com/"):
        proxies_list = []
        i = 0
        
        if ssl:
            ssl = "yes"
        else:
            ssl = "no"

        if download:
            download = "getproxies"
        else:
            download = "displayproxies"

        if not url:
            url = f"https://api.proxyscrape.com/?auth={auth}&request={download}&proxytype={type}&timeout={timeout}&ssl={ssl}&anonimity={anonymity}&country={country}&format={format}".replace(",", "&").replace(" ", "") 

        response = request.urlopen(url).read().decode("utf-8").replace("\r", "")

        for proxy in response.splitlines():
            if number == i:
                break

            if checker:
                try:
                    proxy_handler = request.ProxyHandler({
                    "https": "http://" + proxy,
                    "http": "http://" + proxy,
                    "socks4": "socks4://" + proxy,
                    "socks5": "socks5://" + proxy
                    })

                    opener = request.build_opener(proxy_handler)
                    opener.addheaders = [('User-Agent', 'Mozilla/5.0  (Windows NT 6.1; Win64; x64)')]
                    request.install_opener(opener)

                    response = request.urlopen(request_url, timeout=timeout)
                    proxy_list.append(proxy)

                except:
                    pass

            else:
                proxies.proxies_list.append(proxy)

            i += 1

        if dict:
            proxies_dict = {
            type: type + "://" + proxies.proxies_list
            }

            return proxies_dict

        else:
            return proxies.proxies_list

    def getproxy(dict:bool=False, checker:bool=False, number:int=None, auth:str=None, download:bool=False, type:str="all", country:str="all", timeout:int=1500, ssl:bool=True, anonymity:str="all", format:str="normal", url:str=None, request_url:str="https://google.com/"):
        proxies_list = []
        i = 0

        if ssl:
            ssl = "yes"
        else:
            ssl = "no"

        if download:
            download = "getproxies"
        else:
            download = "displayproxies"

        if not url:
            url = f"https://api.proxyscrape.com/?auth={auth}&request={download}&proxytype={type}&timeout={timeout}&ssl={ssl}&anonimity={anonymity}&country={country}&format={format}".replace(",", "&").replace(" ", "") 

        response = request.urlopen(url).read().decode("utf-8").replace("\r", "")

        for proxy in response.splitlines():
            if number == i:
                break

            if checker:
                try:
                    proxy_handler = request.ProxyHandler({
                    "https": "http://" + proxy,
                    "http": "http://" + proxy
                    })

                    opener = request.build_opener(proxy_handler)
                    opener.addheaders = [('User-Agent', 'Mozilla/5.0  (Windows NT 6.1; Win64; x64)')]
                    request.install_opener(opener)

                    response = request.urlopen(request_url, timeout=timeout)
                    proxy_list.append(proxy)

                except:
                    pass

            else:
                proxies.proxies_list.append(proxy)

            i += 1

        if dict:
            proxies_dict = {
            type: type + "://" + choice(proxies.proxies_list)
            }

            return proxies_dict

        else:
            return choice(proxies.proxies_list)

    def proxies_checker(number:int=None, file:str=None, url:str=None, request_url:str=None, timeout:int=1500):
        i = 0

        proxies_dict = {
            f"file: {file}": [],
            f"url: {url}": []
        }

        if not request_url:
            request_url = "https://google.com/"

        if file:
            with open(file, "r") as f:
                for proxy in f.splitlines():
                    if number:
                        if number == i:
                            break
                    try:
                        proxy_handler = request.ProxyHandler({
                        "https": "http://" + proxy,
                        "http": "http://" + proxy
                        })

                        opener = request.build_opener(proxy_handler)
                        opener.addheaders = [('User-Agent', 'Mozilla/5.0  (Windows NT 6.1; Win64; x64)')]
                        request.install_opener(opener)

                        response = request.urlopen(request_url, timeout=timeout)
                        proxies_dict[f"url: {url}"].append(proxy)
                        i += 1
                    except:
                        pass

        if url:
            response = request.urlopen(url).read().decode("utf-8").replace("\r", "")
            for proxy in response.splitlines():
                if number:
                    if number == i:
                        break
                try:
                    proxy_handler = request.ProxyHandler({
                    "https": "http://" + proxy,
                    "http": "http://" + proxy
                    })

                    opener = request.build_opener(proxy_handler)
                    opener.addheaders = [('User-Agent', 'Mozilla/5.0  (Windows NT 6.1; Win64; x64)')]
                    request.install_opener(opener)

                    response = request.urlopen(request_url, timeout=timeout)
                    proxies_dict[f"url: {url}"].append(proxy)
                    i += 1
                except:
                    pass

        return proxies_dict
