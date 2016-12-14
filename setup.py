from setuptools import setup, find_packages

# Setup file
setup(
    name = 'GreenGraph',
    version = '0.1.0',
    packages = find_packages(exclude=['*tests']),
    scripts = ['scripts/greengraph'],
    install_requires = ['argparse', 'geopy', 'matplotlib', 'mock', 'numpy', 'requests']
)
