import json
import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from src.utilities.utils import get_parent_directory


def dynamic_sql_query(json_file, csv_file):
    json_data = read_json(json_file)
    relationships_df = read_csv(csv_file)
    sql_query = generate_sql_query(json_data, relationships_df)

    return sql_query


def read_json(json_file):
    with open(json_file, 'r') as json_file:
        config = json.load(json_file)
        return config


def read_csv(csv_file):
    relationships_df = pd.read_csv(csv_file)
    return relationships_df


def generate_sql_query(json_data, relationships_df):

    json_tables = set([list(i["table_column_mapping"].keys()) for i in json_data["source_data"]][0])
    
    
    #json_tables = set(json_data["source_data"]['table_column_mapping'].keys())
    relevant_relationships_df = relationships_df[
        (relationships_df['Table1'].isin(json_tables)) & (relationships_df['Table2'].isin(json_tables))
        ]

    if len(json_tables) == len(relevant_relationships_df):
        relevant_relationships_df = relevant_relationships_df.drop(len(relevant_relationships_df) - 1, axis='index')

    parent_directory = get_parent_directory(path=str(os.path.dirname(__file__)),
                                levels=2)
    jinja_file_dir = os.path.join(parent_directory, "templates")

    env = Environment(loader=FileSystemLoader(jinja_file_dir))
    template = env.get_template('template_create_generator.jinja')

    rendered_query = template.render(
        config=json_data,
        relevant_relationships_df=relevant_relationships_df
    )

    return rendered_query
