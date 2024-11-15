import psycopg2
from dotenv import load_dotenv
import os
import json



def run_query(file_path, env, output):
    load_dotenv(env)

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    try:

        with open(file_path, "r") as file:
            query = file.read()

        connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password) 

        cursor = connection.cursor()
        cursor.execute(query)
        rows = list(cursor.fetchall())
        if output == "json":
            rows_json = json.dumps(rows, indent=4)
            return rows_json
        return rows
    except Exception as ex:
        print(ex)

    finally:
      cursor.close()
      connection.close()
    







      









