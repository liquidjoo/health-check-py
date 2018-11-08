import configparser
import requests
import io

config = configparser.ConfigParser()
config.read('config.ini')

# info: Input api setting
api_url: str = config['INPUT_API']['URL']
api_method: str = config['INPUT_API']['METHOD']

# info: Output setting
hosts: str = config['OUT_PUT']['HOSTS']
action: str = config['OUT_PUT']['ACTION']

headers = {
    'Authorization': '',
    'access-token': ''
}

if api_method == 'GET':
    req = requests.get(api_url)

print(req.json())
print(type(req.json()))

