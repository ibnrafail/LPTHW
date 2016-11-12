try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Example project',
    'author': 'Iskandar Gabdrakhmanov',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'faruk.iskandar@yandex.ru',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['myex'],
    'scripts': ['bin/runnable.py'],
    'name': 'myex'
}

setup(**config)
