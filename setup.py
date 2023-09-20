"""
Flask-Mail2
----------

A Flask extension for sending email messages.

Please refer to the online documentation for details.

Links
`````

* `documentation <http://packages.python.org/Flask-Mail>`_
"""
from setuptools import setup

setup(
    name='Flask-Mail2',
    version='1.0.2',
    url='https://github.com/rimvislt/flask-mail2',
    license='BSD',
    author='Dan Jacob',
    author_email='danjac354@gmail.com',
    maintainer='Rimvydas Zilinskas',
    maintainer_email='rim@rdzdirect.com',
    description='Flask extension for sending email',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    py_modules=[
        'flask_mail'
    ],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'blinker',
    ],
    tests_require=[
        'nose',
        'blinker',
        'speaklater',
        'mock',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
