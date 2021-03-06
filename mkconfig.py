import json


def make():
    d = dict()
    d['parent'] = './Projects/'
    d['project'] = 'perlmonks'
    d['project_dir'] = d['parent'] + d['project'] + '/'
    d['base_url'] = 'https://www.perlmonks.org/'
    d['queue'] = d['project_dir'] + 'queue.txt'
    d['crawled'] = d['project_dir'] + 'crawled.txt'
    d['threads'] = 8

    with open('config.json.example', 'w') as f:
        json.dump(d, f)
