import sys
import os


from src.utilities import get_parent_directory
from src.cli import dynamic_sql_query
from src.cli import argument_parser


def main():
    parent_dir_path = get_parent_directory(path = str(os.path.dirname(__file__)),
                                           levels=1)
    file_path = os.path.join(parent_dir_path, "tables_relationships.csv")

    args=argument_parser()

    #json_file = r"C:\Users\amit.sahoo\OneDrive - Argo Group\DAL\Prototype\DAL_POC\sample3.json"

    sql_query = dynamic_sql_query(args.json_file,
                                  #json_file,
                                  file_path)
    #print(sys.path)
    print(sql_query)



if __name__ == "__main__":
    main()
    #print(sys.path)

