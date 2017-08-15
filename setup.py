#!/usr/bin/python
import os
import shutil
import site
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
<<<<<<< HEAD
'''
Install domainchecker files and default wordslist. Touches a whitelist file by default.

'''
os.mkdir('/opt/domainchecker') 
shutil.move('badwords', '/opt/domainchecker/badwords') 
os.mknod('/opt/domainchecker/whitelist') 
  
=======
# Install domainchecker files/wordslist
if not os.path.exists("/opt/"):
    os.mkdir("/opt")

if not os.path.exists("/opt/domainchecker"):
    os.mkdir("/opt/domainchecker")

shutil.move('badwords', '/opt/domainchecker/')
>>>>>>> 911466cf264e167ed749fcb62d034c74394f8d75
