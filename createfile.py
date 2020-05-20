import requests
import base64
from getpass import getpass

username = input('Enter your name: ')
password = getpass()

content = 'Working GitHub API'
b_content = content.encode('utf-8')
base64_content = base64.b64encode(b_content)
base64_content_str = base64_content.decode('utf-8')
print(base64_content_str)