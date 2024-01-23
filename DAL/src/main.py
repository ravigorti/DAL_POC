import sys
from cli.commands.json_file import json_file
from cli.argumentParser import argument_parser
from exceptions import CustomException
from logger import logging

if __name__ == "__main__":
    args=argument_parser()
    json_file(args.json_file)

