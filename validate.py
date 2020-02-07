import yaml

with open('./config.yaml') as fd:
    yaml.safe_load(fd)
    print('YAML successfully parsed')
