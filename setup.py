from setuptools import setup, find_packages

# Setup file
setup(
    name = 'GreenGraph',
    version = '0.1.0',
    description= 'Plot showing green pixel distribution between two locations using Google Maps.',
    author= 'Dimitri Visnadi - MPHYG001 - Univeristy College London'
    packages = find_packages(exclude=['*tests']),
    scripts = ['scripts/greengraph'],
    install_requires = ['argparse', 'geopy', 'matplotlib', 'numpy', 'requests', 'seaborn']
)
