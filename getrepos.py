import requests
from getpass import getpass

username = input('Enter your name: ')
password = getpass()
string = 'https://api.github.com/user/repos'

r = requests.get(string, auth=(username, password))
print(r.json())