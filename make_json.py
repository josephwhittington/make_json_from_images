# Title: make_json
# Author: Joseph Whittington
# Dependencies: python 2.7.*, runs on native installation of Mac OSX+ 

# Description: This program generates a json file with filenames of images found 
#              in the directory of the make_json.py file as the suppilied first 
#              argument when running the script. The generated file gets optput
#                in the directory of the script

# **run the program by typing "python make_json.py with valid flag arguments"

# valid arguments:[
#     --first=<filename_property>,
#     --output=<json_file_name>,
#     --additional=propOne,propTwo
# ]

# --first this is the name of the property that will have the value of the image names
# --output will be the name of the json file generated
# --additional takes in comma separated values and uses those arguments as additional fields 
#   in the json file with empty values, don't use spaces because that would be separate 
#   arguments


import os
import json
from sys import argv

def main(argv):
    parsed_args = parse_args(argv)

    file_name_prop = parsed_args['first']

    extentions_to_check = ['.jpg', '.jpeg', '.png']
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_obj = []

    for file_name in os.listdir(dir_path):
        if any(ext in file_name for ext in extentions_to_check):
            working_obj = {file_name_prop: file_name}
            if parsed_args['additional']:
                for arg in parsed_args['additional']:
                    working_obj[arg] = ""
            json_obj.append(working_obj) 
    make_json(json_obj, parsed_args['out'])

# saves the output to a json file
def make_json(obj, out):
    f = open(out, 'w+')
    f.write(json.dumps(obj))
    f.close()

# parses the arguments into usable blocks
def parse_args(args):
    flags = ['--first', '--additional', '--output']
    configs = {
        'first': '',
        'out': '',
        'additional': []
    }
    # loop through the arguments and look for flags
    for arg in args:
        if any(flag in arg for flag in flags):
            if '--first' in arg: 
                configs['first'] = arg[arg.index('=')+1:]
            elif '--output' in arg:
                configs['out'] = arg[arg.index('=')+1:] + '.json'
            elif '--additional' in arg:
                additional_args = arg[arg.index('=')+1:].split(',')
                configs['additional'] = additional_args
    return configs

# Standard convention that allows the code to be run only when invoked or if the file is running as a program rather than an import
if __name__ == '__main__':
    main(argv)