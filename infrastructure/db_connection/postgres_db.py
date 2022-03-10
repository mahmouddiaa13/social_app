import psycopg2

def get_postgres_conn(localhost: str, db_name: str, user_name:str):
    conn = psycopg2.connect(host=localhost, database=db_name, user= user_name)