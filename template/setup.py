try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'discription': 'My Project',
'author': 'Jamila Grote',
'url': 'URL to get it at.',
'download_url' : 'Where to fownload it.',
'author_email'; 'jamilagrote@stud.leuphana.de',
'version': '0.1',
'install_requires': ['nose'],
'packages':['NAME'],
'scripts': [],
'name': 'projectname'
}

setup(**config)
