import sqlite3

# Connect to the database file (or create it if it does not exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# TODO: Create the students table

# TODO: Insert at least three students into the table

# TODO: Query all students and print the results

# TODO: Query students with grade above a threshold and print those results

# Close the connection when finished
conn.close()
