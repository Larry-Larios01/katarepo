import psycopg2
from dotenv import load_dotenv
import os



host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

def count_tickets_per_status():
    try:
        connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password) 

        cursor = connection.cursor()
        print("--    count of tickets per status  --columns - status_name,	ticket_count")
        cursor.execute("select ts.name as status,count(t.id) count_of_tickets from ticketit t inner join ticketit_statuses ts on t.status_id  = ts.id group by ts.id ")
        rows = cursor.fetchall()
        for row in rows:
          print(row)
    except Exception as ex:
        print(ex)

    finally:
      cursor.close()
      connection.close()
    


def amount_tickets_per_agent_and_their_status():
    try:
        connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password) 

        cursor = connection.cursor()
        print("amount of tickets per agent and their status:")
        cursor.execute("select t.agent_id as agent , count(t.id) amount_tickets, ts.name status from ticketit t inner join ticketit_statuses ts on t.status_id  = ts.id group by t.agent_id, ts.name")
        rows = cursor.fetchall()
        for row in rows:
          print(row)
    except Exception as ex:
        print(ex)

    finally:
      cursor.close()
      connection.close()


count_tickets_per_status()

amount_tickets_per_agent_and_their_status()
      









