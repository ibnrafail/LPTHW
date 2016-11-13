try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise #48',
    'author': 'Iskandar Gabdrakhmanov',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'faruk.iskandar@yandex.ru',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)
