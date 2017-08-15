#!/usr/bin/python
import os
import shutil
from setuptools import setup

# Domain checker setup
setup(
    name = "Domain Checker",
    version = "0.1",
    author = "Riley",
    author_email = "riley@fasterdevops.com",
    url = "https://github.com/sadminriley/domainchecker",
    license = "MIT",
)
'''
Install domainchecker files and default wordslist. Touches a whitelist file by default.

'''
os.mkdir('/opt/domainchecker') 
shutil.move('badwords', '/opt/domainchecker/badwords') 
os.mknod('/opt/domainchecker/whitelist') 
  
