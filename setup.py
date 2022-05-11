from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='python-color-getter',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description="Python color getter (including method to get random color or complementary color)",
    url='https://github.com/yjg30737/python-color-getter.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
)