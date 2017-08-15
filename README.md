# domainchecker
A tool that checks potentially fraud domains against a 'badwords' list for cPanel servers.

# setup
```
python setup.py install
```
This creates the directory /opt/domainchecker, moves the provided badwords list to the directory, and touches a whitelist file.

# usage
Each list entry must be on a new line in the badwords and whitelist file.

