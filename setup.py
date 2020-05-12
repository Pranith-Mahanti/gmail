#!/usr/bin/env python3.7
from setuptools import setup, find_packages

setup(
    name='mailto',
    version='1.0',
    description='Send mails easily from terminal',
    url='',
    author='Pranith Mahanti',
    author_email='',
    license='',
    install_requires=['smtplib', 'sys'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['rq=src.main:send_mail']
    )
)
