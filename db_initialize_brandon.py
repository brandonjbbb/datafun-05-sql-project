import sqlite3


def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, "r") as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")


def main():
    db_file = "my_database.db"  # Name your database file
    sql_file = "create_tables.sql"
    execute_sql_from_file(db_file, sql_file)


if __name__ == "__main__":
    main()
