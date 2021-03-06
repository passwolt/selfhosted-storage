import os
from setuptools import setup


README_PATH = os.path.join(os.path.dirname(__file__), 'README.md')
with open(README_PATH) as f:
    README_DATA = f.read()


# This call to setup() does all the work
setup(
    name                          = 'passwolt-server',
    version                       = '0.0.1',
    description                   = 'Passwolt\'s password storage server (self hosted ed.)',
    long_description              = README_DATA,
    long_description_content_type = 'text/markdown',
    url                           = 'https://github.com/passwolt/selfhosted-storage',
    author                        = 'return007',
    author_email                  = 'glalchandanig@gmail.com',
    packages                      = ['passwolt_server'],
    python_requires               = '>=3.6',
    license                       = 'MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Security',
    ],
    install_requires = [
    ],
    entry_points = {
        'console_scripts': [
            'passwolt-server=passwolt_server.main:main',
        ]
    },
)
