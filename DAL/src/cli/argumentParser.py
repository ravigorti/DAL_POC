import argparse
def argument_parser():
    parser = argparse.ArgumentParser(description='Database Query CLI')
    parser.add_argument('--json_file', type=str, help='Path to the JSON configuration file')
    args = parser.parse_args()
    return args

# def load_file(json_file):
#     with open(json_file, 'r') as json_file:
#         json_config = json.load(json_file)
#         db_query = DatabaseQuery(json_config)
#         db_query.execute_query()
