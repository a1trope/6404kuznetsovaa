from setuptools import setup

setup(
   name='data_analysis',
   version='1.0',
   description='A useful module',
   author='Sanya',
   author_email='sanya@gmail.com',
   packages=['data_analysis'],
   install_requires=['pandas', 'numpy', 'meteostat', 'flake8'],
)