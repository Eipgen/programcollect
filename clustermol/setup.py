import clusterfps
from setuptools import setup
from setuptools import find_packages

setup(
    name = "CLF",
    version = "v0.1.0",
    description = "cluster",
    author = "Jinxiao",
    packages = find_packages(),
    platforms = "any",
    install_requires = ["requests", 
                        "docopt>=0.6.2",
                        ],
    entry_points = {"console_scripts": ['CLF = clusterfps.clusfps_v1:main']}
)
