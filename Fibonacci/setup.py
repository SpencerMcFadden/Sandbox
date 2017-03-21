try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Index finder for fibonacci sequence',
    'author': 'Spencer McFadden',
    'url': 'https://github.com/SpencerMcFadden/Sandbox/tree/master/Fibonacci',
    'download_url': 'https://github.com/SpencerMcFadden/Sandbox/tree/master/Fibonacci',
    'author_email': 'spencer.v.mcfadden@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['fibFinder'],
    'scripts': [],
    'name': 'fibFinder'
}

setup(**config)
