import sqlite3


def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, "r") as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")


def query_data(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, "r") as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed query from {sql_file}")


def main():
    db_file = "my_database.db"

    sql_join_file = "query_join.sql"
    sql_sort_file = "query_sorting.sql"
    sql_aggregation_file = "query_aggregation.sql"

    query_data(db_file, sql_join_file)  # Perform join query
    query_data(db_file, sql_sort_file)  # Perform sorting query
    query_data(db_file, sql_aggregation_file)  # Perform aggregation query


if __name__ == "__main__":
    main()
