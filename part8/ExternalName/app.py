import psycopg2
import os
import sys

def main():
    db_host = os.getenv("DATABASE_HOST")
    db_port = os.getenv("DATABASE_PORT")
    db_user = os.getenv("DATABASE_USER", "postgres")
    db_password = os.getenv("DATABASE_PASSWORD", "example")
    db_name = os.getenv("DATABASE_NAME", "postgres")

    conn_string = f"host={db_host} port={db_port} dbname={db_name} user={db_user} password={db_password}"
    print("Connecting to database\n ->%s" % conn_string)

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        print("Connected!\n")
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"Database version: {version[0]}")
    except Exception as e:
        print("Unable to connect to the database.")
        print(e)
        sys.exit(1)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
