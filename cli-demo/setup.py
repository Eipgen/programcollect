#encoding utf-8

from pkg import __version__
from setuptools import setup
from setuptools import find_packages

setup(
    name = "CliDemo",
    version = __version__,
    description = "Command line Demo",
    author = "betester",
    packages = find_packages(),
    platforms = "any",
    install_requires = ["requests", 
                        "docopt>=0.6.2"
                        ],
    entry_points = {"console_scripts": ['clidemo = pkg.hello:cmd']}
)
