#summary of the project
This project is a hands-on experience in  data modelling with Postgre and building ETL pipeline with Python to extract and transform  files  in JSON format and then load them structured into the Sparkify Database .
The Star schema served me well. One fact table (songplays) and four Dimension tables (users,songs,artists,time) were created in the Sparkify Database.
The ETL pipeline is used to transfer files from two directories (/log_data, /song_data) into database tables with the help of Python and SQL.
a summary of the project

#How i ran the Python scripts
create_tables.py: From the "Project Workspace", call up the Terminal by going to File --> New --> Terminal and enter and run "Python create_tables.py" to drop the five tabes if they exist, create them new and insert data into them. There is autocommit set during the creation of Sparkify Database. So no manual commit needed.

etl.py: Run "Python etl.py" in the terminal to process all the data.

test.ipynb: runs in the Jupiter notebook and checks whether the tables were created with the right columns. But it doesnt check whether the Datatype is correct or not. 
an explanation of the files in the repository

#An explanation of the files in the repository
sql_queries.py: drop and create table, insert into tables, update records.
Create_tables.py: Master scripts that calls sql_queries.py
etl.py: processes all datasets.
etl.ipynb: loads date from /log_data, /song_data into the tables
test.ipynb: Confirms that the tables were created without errors.

#State and justify your database schema design and ETL pipeline.
As mentioned in the project summary, there are one fact table referencing four dimention tables. The chosen ETL pipeline enables the seamless transfer of data into the database tables
