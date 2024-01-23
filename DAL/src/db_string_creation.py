class DatabaseQuery:
    def __init__(self, json_config):
        self.json_config = json_config

    def generate_sql_query(self):
        template_str = """
        SELECT {{ fields }}
        FROM {{ table }}
        {% if conditions %}
        WHERE
            {% for key, condition in conditions.items() %}
                {% if condition is string %}
                    {{ key }} = '{{ condition }}'
                {% else %}
                    {{ key }} {{ condition.operator }} {{ condition.value }}
                {% endif %}
                {% if not loop.last %} AND {% endif %}
            {% endfor %}
        {% endif %}
        """
        template = jinja2.Template(template_str)
        sql_query = template.render(self.json_config)
        return sql_query

    def execute_query(self):
        sql_query = self.generate_sql_query()
        print("Generated SQL Query:", sql_query)

        conn = sqlite3.connect('mydatabase.sqlite')
        cursor = conn.cursor()
        cursor.execute(sql_query, self.json_config.get('conditions', {}))
        results = cursor.fetchall()
        print("Query Results:", results)

        conn.commit()
        conn.close()