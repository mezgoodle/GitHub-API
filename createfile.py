import requests
import base64
from getpass import getpass

username = input('Enter your name: ')
password = getpass()

content = 'Working GitHub API'
b_content = content.encode('utf-8')
print(b_content)