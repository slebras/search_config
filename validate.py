import yaml

with open('./config.yaml') as fd:
    yaml.load(fd)
    print('YAML successfully parsed')
