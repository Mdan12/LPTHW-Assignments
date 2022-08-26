try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Advanced User Input',
    'author': 'Magnús Daníel Budai Einarsson',
    'url': 'www.pianostillingarMD.is',
    'download_url': 'www.pianostillingarMD.is/downloads',
    'author_email': 'magnusde93@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
