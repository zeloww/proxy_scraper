from setuptools import setup

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
    name='proxy-scraper',
    version='1.0',
    license='GNU',
    authors=['zelow'],
    description='Get any type of proxies in 1 click!',
    long_description=long_description,
    keywords=['python', 'py', 'proxy', 'proxies', 'getproxy', 'getproxies', 'proxy-scraper', 'proxies-scraper', 'scraper'],
    packages=['proxy-scraper']
)