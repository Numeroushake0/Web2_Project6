from data.create_db import create_tables
from data.seed_db import seed
from data.db_connection import create_connection
import os

def execute_sql_file(filename):
    conn = create_connection()
    cur = conn.cursor()
    with open(filename, "r") as f:
        sql = f.read()
    for statement in sql.strip().split(";"):
        if statement.strip():
            cur.execute(statement)
            rows = cur.fetchall()
            for row in rows:
                print(row)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    seed()
    for file in sorted(os.listdir("queries")):
        if file.endswith(".sql"):
            print(f"\n--- {file} ---")
            execute_sql_file(os.path.join("queries", file))
