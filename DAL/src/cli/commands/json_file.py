import json
import pandas as pd
from jinja2 import Environment, FileSystemLoader
def dynamic_sql_query(json_file,csv_file):
   json_data = read_json(json_file)
   relationships_df = read_csv(csv_file)
   sql_query = generate_sql_query(json_data,relationships_df)

   return sql_query


def read_json(json_file):
   with open(json_file, 'r') as json_file:
      config = json.load(json_file)
      return config
     
def read_csv(csv_file):
   relationships_df = pd.read_csv(csv_file)
   return relationships_df


def generate_sql_query(json_data, relationships_df):
      
      if relationships_df is None or len(relationships_df) == 0:
         print('No relevant relationships found!')
         return None
      json_tables = set(json_data['columns'].keys())
      relevant_relationships_df = relationships_df[
        (relationships_df['Table1'].isin(json_tables)) & (relationships_df['Table2'].isin(json_tables))
    ]
      print(relevant_relationships_df)
      if len(json_tables)==len(relevant_relationships_df):
          relevant_relationships_df = relevant_relationships_df.drop(len(relevant_relationships_df)-1,axis='index')

      print(relevant_relationships_df)
      env = Environment(loader=FileSystemLoader(r'/Users/ravitejagorti/Desktop/final_framework/DAL/DAL/src/templates'))
      template = env.get_template('template_sql_generator.jinja')
      
      rendered_query = template.render(
         config=json_data,
         relevant_relationships_df=relevant_relationships_df
      )
      
      return rendered_query




    