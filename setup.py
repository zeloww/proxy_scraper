import io
from setuptools import setup

with io.open('README.md', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='proxy_scraper',
    version='1.8',
    license='GPLv3+',
    authors=['zelow'],
    url="https://github.com/zeloww/proxy_scraper",
    description='Get any type of proxies in 1 click!',
    long_description=long_description,
    keywords=['python', 'py', 'proxy', 'proxies', 'getproxy', 'getproxies', 'proxy-scraper', 'proxies-scraper', 'scraper'],
    packages=['proxy_scraper']
)
