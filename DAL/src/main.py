import sys
from cli.commands.json_file import dynamic_sql_query
from cli.argumentParser import argument_parser
from exceptions import CustomException
from logger import logging

if __name__ == "__main__":
    args=argument_parser()
    sql_query = dynamic_sql_query(args.json_file,r'/Users/ravitejagorti/Desktop/final_framework/DAL/tables_relationships.csv')
    print(sql_query)

