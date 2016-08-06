#!/usr/bin/env python


from setuptools import setup


setup(
    name='mdx_quote',
    version='1.0',
    author='Dingyuan Wang',
    description='Python-Markdown extension to support the <q> tag.',
    py_modules=['mdx_quote'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
