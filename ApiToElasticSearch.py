import configparser
import requests
# pip install requests, when your code make an Error

config = configparser.ConfigParser()
config.read('config.ini')

# info: Input api setting
if "IN.API" in config:
    api_url: str = config['IN.API']['URL']
    api_method: str = config['IN.API']['METHOD']

# Api Method Header setting for make custom
# input condition
if api_method == 'GET':
    req = requests.get(api_url)

# info: Output setting for Elasticsearch
if "OUT.ES" in config:
    import datetime
    hosts: str = config['OUT.ES']['HOSTS']
    action: str = config['OUT.ES']['ACTION']
    index = "logstash-health"+datetime.datetime.now().strftime('%Y-%m-%d')
    doc_type: str = config['OUT.ES']['DOCUMENT_TYPE']
    headers = {
        # 'Authorization': '',
        # 'access-token': '',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    # output condition
    if action == 'index':
        body: dict = req.json()
        print(body)
        hosts = "{}/{}/{}".format(hosts, index, doc_type)
        response = requests.post(url=hosts, json=body, headers=headers)


