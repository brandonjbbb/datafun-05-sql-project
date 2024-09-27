import sqlite3


def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, "r") as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")


def insert_data(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, "r") as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Inserted data from {sql_file}")


def update_data(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, "r") as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Updated records from {sql_file}")


def delete_data(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, "r") as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Deleted records from {sql_file}")


def query_data(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, "r") as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed query from {sql_file}")


def main():
    db_file = "my_database.db"
    sql_create_file = "create_tables.sql"
    sql_insert_file = "insert_records.sql"
    sql_update_file = "update_records.sql"
    sql_delete_file = "delete_records.sql"
    sql_query_file = "query_filter.sql"

    execute_sql_from_file(db_file, sql_create_file)  # Create tables
    insert_data(db_file, sql_insert_file)  # Insert data
    update_data(db_file, sql_update_file)  # Update data
    delete_data(db_file, sql_delete_file)  # Delete data
    query_data(db_file, sql_query_file)  # Query data


if __name__ == "__main__":
    main()
