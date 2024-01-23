import json
def json_file(json_file):
     with open(json_file, 'r') as json_file:
        config = json.load(json_file)
        print(config)
        return config