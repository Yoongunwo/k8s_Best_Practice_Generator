import yaml
import json
import os
import sys

def yamlToJson() :
    # Convert yaml file to json data
    with open(sys.argv[1], 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            print(data)
        except yaml.YAMLError as exc:
            print(exc)
    

if __name__ == "__main__" :
    yamlToJson()