import requests
from getpass import getpass

username = input('Enter your name: ')
password = getpass()
string = 'https://api.github.com/user'

r = requests.get(string, auth=(username, password))
print(r.text)