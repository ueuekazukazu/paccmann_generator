"""Install package."""
from setuptools import setup, find_packages
import os
import codecs


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError('Unable to find version string.')


setup(
    name='paccmann_generator',
    version=get_version('paccmann_generator/__init__.py'),
    description='Multimodal generative models for PaccMann^RL.',
    long_description=open('README.md').read(),
    url='https://github.com/PaccMann/paccmann_generator',
    author='Jannis Born, Matteo Manica, Ali Oskooei, Joris Cadow',
    author_email=(
        'jab@zurich.ibm.com, drugilsberg@gmail.com, '
        'ali.oskooei@gmail.com, joriscadow@gmail.com'
    ),
    install_requires=[
        'numpy', 'pandas', 'matplotlib', 'seaborn',
        'pytoda @ git+ssh://git@github.com/PaccMann/paccmann_datasets@1.1.2',
        'torch>=1.0.0', 'six>=1.12.0',
        'toxsmi @ git+ssh://git@github.com/ueuekazukazu/chemical_representation_learning_for_toxicity_prediction.git'
    ],
    packages=find_packages('.'),
    zip_safe=False,
)
