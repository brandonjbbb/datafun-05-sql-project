import sqlite3
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(
    filename="log.txt",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def execute_sql_from_file(db_filepath, sql_file):
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL from {sql_file}")
    except Exception as e:
        logging.exception(f"Error executing SQL from {sql_file}: {e}")


def query_data(db_filepath, sql_file):
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed query from {sql_file}")
    except Exception as e:
        logging.exception(f"Error executing query from {sql_file}: {e}")


def main():
    db_file = "my_database.db"

    sql_join_file = "query_join.sql"
    sql_sort_file = "query_sorting.sql"
    sql_aggregation_file = "query_aggregation.sql"

    logging.info("Starting SQL operations")

    query_data(db_file, sql_join_file)  # Perform join query
    query_data(db_file, sql_sort_file)  # Perform sorting query
    query_data(db_file, sql_aggregation_file)  # Perform aggregation query

    logging.info("SQL operations completed successfully")


if __name__ == "__main__":
    logging.info("Program started")
    main()
    logging.info("Program ended")
