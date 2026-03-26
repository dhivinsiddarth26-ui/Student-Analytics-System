import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="datascience_db",
        user="postgres",
        password="dhivin08"
    )
    return conn