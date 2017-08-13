#!/usr/bin/python

'''
This script checks domains in /etc/trueuserdomains
and looks for obvious fraud or phishing domains
on cPanel servers.

'''
from smtplib import SMTP

__version__ = 'v0.1 Fraud Domain Checker'
__author__ = 'Riley'


def main():
    '''
   Checks for suspicious domain names on cPanel servers
   and sends an email notification if any are found.
   Both the badwords and whitelist are stored in a plain text file,
   with each word on a new line. May use a json format eventually.
   '''

    match_found = False
    definitions = []
    with open("/opt/domainchecker/badwords") as definitions_file:
        for line in definitions_file:
            definitions.append(line.strip())

    matches = []
    match_text = ""
    whitelist = []
    with open("/opt/domainchecker/whitelist", "r") as whitelist_file:
        for line in whitelist_file:
            whitelist.append(line.strip())

    '''
    Opens /etc/trueuserdomains and checks every line from the badwords list.
    Matches found that are in the whitelist are ignored

    '''
    with open("/etc/trueuserdomains", "r") as domains:
        for line in domains:
            for item in definitions:
                if any(item in string for string in whitelist):
                    pass
                elif item in line:
                    match_text = 'Match: ' + line + 'contains\n ' + item
                    matches.append(match_text)
                    match_found = True

    # If matches are found,send a notification via smtplib.
    if match_found:
        sendmail = SMTP()
        sendmail.connect('email.server.com', 25)
        sendmail.login('serveremail@hostname.com', 'password123')
        from_addr = 'serversemail@hostname.com'
        to_addr = 'notify@youradmin.com'
        subject = 'Possible fraudulent or phishing domains found!'
        msg = ('The following domains contain keywords that may be ' +
               'fraudulent activity- \n \n ' + match_text)
        sendmail(from_addr, to_addr, subject, msg)

if __name__ == "__main__":
    main()
