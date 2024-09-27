Project Overview

This project demonstrates how to use Python to interact with a SQL database. The project is built using SQLite for managing relational data and incorporates Python packages like pandas for data manipulation.

Features:
Create and manage a relational database using SQLite.
Perform various SQL operations including inserting, updating, deleting, joining, sorting, and aggregating data.
Log program execution using Python's built-in logging module.
View SQL queries and results in a clear, structured format.
How to Run the Project

Prerequisites
Python 3.6+: Make sure you have Python installed. You can download it here.
Packages: You need to install pandas and pyarrow. Run the following command to install them:
bash
Copy code
pip install pandas pyarrow
Step 1: Clone the Repository
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/brandonjbbb/datafun-05-sql-project.git
cd datafun-05-sql-project
Step 2: Set Up the Virtual Environment (Optional but recommended)
It’s a good practice to use a virtual environment to manage dependencies separately for each project. Here’s how to set up and activate one:

On Mac/Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
On Windows:
bash
Copy code
python -m venv venv
.\venv\Scripts\activate
Step 3: Execute the Project
After cloning the repo and setting up the environment, follow these steps to run the project:

Create the Database and Insert Data: Run the following command to execute the script and create the SQLite database, insert sample data, and run some SQL operations:
bash
Copy code
python db_initialize_brandon.py
What Happens When You Run the Script:
Table Creation: The create_tables.sql script will create the necessary tables.
Data Insertion: The insert_records.sql script will populate the tables with sample data.
Update, Delete, and Query: Various SQL operations, such as updating records, deleting records, and querying data, will be executed using the respective SQL scripts:
update_records.sql
delete_records.sql
query_join.sql
query_sorting.sql
query_aggregation.sql
Logging: The script will log every operation in the log.txt file for debugging and tracking purposes.
Step 4: View the Results
View Database: After running the script, the SQLite database (my_database.db) will be created. You can view the data in this file by using a tool like DB Browser for SQLite.
Log File: You can check the log.txt file for a detailed log of what happened during execution. Each SQL operation will be logged with timestamps for debugging or auditing purposes.
Project Workflow

Commands to Run the Project:
Set Up and Activate Virtual Environment:
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # For Mac/Linux

# For Windows:
python -m venv venv
.\venv\Scripts\activate
Install Dependencies:
bash
Copy code
pip install pandas pyarrow
Run the Main Script:
bash
Copy code
python db_initialize_brandon.py
View the Logs: Open the log.txt file to see the logged SQL operations:
bash
Copy code
cat log.txt
Database Operations Performed:
Table Creation: The following tables are created:
authors (with columns author_id, first_name, last_name, birthdate)
books (with columns book_id, title, published_year, author_id)
Insert Records: Sample data is inserted into both the authors and books tables.
SQL Operations:
Update: update_records.sql updates specific data in the books table.
Delete: delete_records.sql deletes specific records from the authors table.
Join: query_join.sql performs an inner join between authors and books.
Sorting: query_sorting.sql sorts the books by published_year.
Aggregation: query_aggregation.sql performs aggregations like counting total books and calculating the average published year.
SQL Files in This Project:

create_tables.sql: Creates the authors and books tables.
insert_records.sql: Inserts initial records into the tables.
update_records.sql: Updates specific records in the database.
delete_records.sql: Deletes specific records from the database.
query_join.sql: Performs a join operation to fetch records from multiple tables.
query_sorting.sql: Sorts records based on specific fields.
query_aggregation.sql: Performs aggregation functions like COUNT and AVG.
Conclusion

This project showcases how Python and SQL can be used together to interact with relational databases. It demonstrates SQL operations like creating, inserting, updating, deleting, sorting, joining, and aggregating data, all while logging important actions for debugging and record-keeping.