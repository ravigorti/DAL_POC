import sys
import os
from cli.commands.json_file import dynamic_sql_query
from cli.argumentParser import argument_parser
from utils import get_parent_directory
#from exceptions import CustomException
#from logger import logging


def main():
    parent_dir_path = get_parent_directory(path = str(os.path.dirname(__file__)),
                                           levels=2)
    file_path = os.path.join(parent_dir_path, "tables_relationships.csv")

    #args=argument_parser()
    json_file = r"C:\Users\amit.sahoo\OneDrive - Argo Group\DAL\Prototype\DAL_POC\sample3.json"
    sql_query = dynamic_sql_query(#args.json_file,
                                  json_file,
                                   file_path)
    print(sql_query)


if __name__ == "__main__":
    main()
    
    

    



