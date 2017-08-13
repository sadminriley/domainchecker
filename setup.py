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
# Install domainchecker files/wordslist
if not os.path.exists("/opt/"):
    os.mkdir("/opt")

if not os.path.exists("/opt/domainchecker"):
    os.mkdir("/opt/domainchecker")

if not os.path.exists("/opt/domainchecker/badwords"):
    os.mkdir("/opt/domainchecker/badwords")

shutil.move('badwords', '/opt/domainchecker/badwords')
