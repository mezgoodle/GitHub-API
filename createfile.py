import requests
import base64
from getpass import getpass

username = input('Enter your name: ')
password = getpass()

content = 'Working GitHub API'
b_content = content.encode('utf-8')
base64_content = base64.b64encode(b_content)
print(base64_content)