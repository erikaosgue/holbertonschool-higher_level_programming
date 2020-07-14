# 0x0D. SQL - Introduction

## Resources:books:

Read or watch:

* [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
* [Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
* [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
* [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
* [MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html)

# Learning Objectives:bulb:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

## Requirements

### General
* Allowed editors: vi, vim, emacs
* All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A README.md file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using wc

## Tasks

[0. List databases](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/0-list_databases.sql)

Write a script that lists all databases of your MySQL server.

[1. Create a database](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/1-create_database_if_missing.sql)

Write a script that creates the database hbtn_0c_0 in your MySQL server.

[2. Delete a database](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/2-remove_database.sql)

Write a script that deletes the database hbtn_0c_0 in your MySQL server.

[3. List tables](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/3-list_tables.sql)

Write a script that lists all the tables of a database in your MySQL server.

[4. First table](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/4-first_table.sql)

Write a script that creates a table called first_table in the current database in your MySQL server.

[5. Full description](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/5-full_table.sql)

Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

[6. List all in table](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/6-list_values.sql)

Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

[7. First add](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/7-insert_value.sql)

Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

* New row:
* * id = 89
* * name = Holberton School
* The database name will be passed as an argument of the mysql command

[8. Count 89](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/8-count_89.sql)

Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

[9. Full creation](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/9-full_creation.sql)

Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

[10. List by best](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/10-top_score.sql)

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

[11. Select the best](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/11-best_score.sql)

Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the mysql command

[12. Cheating is bad](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/12-no_cheating.sql)

Write a script that updates the score of Bob to 10 in the table second_table.
* You are not allowed to use Bob’s id value, only the name field
* The database name will be passed as an argument of the mysql command

[13. Score too low](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/13-change_class.sql)

Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

[14. Average](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/14-average.sql)

Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

* The result column name should be average
* The database name will be passed as an argument of the mysql command

[15. Number by score](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/15-groups.sql)

Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

* The result should display:
    * the score
    * the number of records for this score with the label number
* The list should be sorted by the number of records (descending)
* The database name will be passed as an argument to the mysql command

[16. Say my name](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/16-no_link.sql)

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

* Don’t list rows without a name value
* Results should display the score and the name (in this order)
* Records should be listed by descending score
* The database name will be passed as an argument to the mysql command

[17. Go to UTF8](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/100-move_to_utf8.sql)

Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

You need to convert all of the following to UTF8:

* Database hbtn_0c_0
* Table first_table
* Field name in first_table

[18. Temperatures #0](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/101-avg_temperatures.sql)

Import in hbtn_0c_0 database this table dump: download

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

[19. Temperatures #1](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/102-top_city.sql)

Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)

Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

[20. Temperatures #2](https://github.com/erikaosgue/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/103-max_state.sql)

Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)

Write a script that displays the max temperature of each state (ordered by State name).






