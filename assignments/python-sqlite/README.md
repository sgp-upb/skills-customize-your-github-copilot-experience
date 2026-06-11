# 📘 Assignment: Python and SQLite Databases

## 🎯 Objective

Learn how to use Python with SQLite to create and query a simple database. Students will build a small program that stores records, retrieves data with SQL, and shows how applications keep data persistently.

## 📝 Tasks

### 🛠️ Database Setup and Table Creation

#### Description
Create a SQLite database and define a table for storing student records.

#### Requirements
Completed program should:

- Create or connect to an SQLite database file.
- Create a table named `students` with columns `id`, `name`, and `grade`.
- Use a cursor to execute the table creation SQL.

### 🛠️ Insert Records

#### Description
Add student records to the database using Python and parameterized SQL statements.

#### Requirements
Completed program should:

- Insert at least three students into the `students` table.
- Use parameterized queries to safely add the data.
- Commit the transaction after inserting records.

### 🛠️ Query Data

#### Description
Read data back from the database and print filtered results.

#### Requirements
Completed program should:

- Query all student records from the `students` table.
- Query only students with a grade above a chosen threshold.
- Print query results in a readable format.
