from setuptools import setup
setup(
name = 'release0_1',
version = '0.1',
install_requires = ['Click','urllib3','colorama'],
py_modules = ['release0_1'],

entry_points={
'console_scripts':
['release0_1=release0_1:cli']}
)
