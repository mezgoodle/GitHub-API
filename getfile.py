import requests
from getpass import getpass

username = input('Enter your name: ')
password = getpass()

repo = input('Repo: ')
# If you want only readme file
# GET /repos/:owner/:repo/readme
# If you want other file
file_path = 'README.md'
print(username, repo)
string = f'https://api.github.com/repos/{username}/{repo}/contents/{file_path}'
print(string)
file_response = requests.get(string)
print(file_response.json())