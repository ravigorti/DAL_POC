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

    sql_query = dynamic_sql_query(#args.json_file,
                                  args.json_file,
                                  file_path)
    review_query = input("\n\nGenerated SQL Query:\n\n\n" +'\33[33m' +sql_query +'\033[0m' +"\n\nProceed to execute the query? (yes/no): ").lower()
    if review_query == 'yes':
            # Execute the SQL query
            execute_query(sql_query)
    else:
        print("SQL query execution aborted.")

    #print(sys.path)

def execute_query(sql_query):
     #use snowflake-python connector here
     print("return the snowflake execution status here")

if __name__ == "__main__":
    main()
    #print(sys.path)

