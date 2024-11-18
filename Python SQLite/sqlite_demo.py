import sqlite3

from Employee import Employee

connection = sqlite3.connect('employee.db')

cursor = connection.cursor()

CREATE_TABLE = """CREATE TABLE employees (
                    first TEXT,
                    last TEXT,
                    pay INTEGER
                    
                )"""

emp_1 = Employee('Raja', 'K', 4000)

emp_2 = Employee('Kumar', 'S', 6000)

INSERT_ROW = """INSERT INTO employees VALUES ('{}', '{}', {});""".format(emp_1.first, emp_1.last, emp_1.pay)

SELECT = """SELECT * FROM employees"""

cursor = connection.execute(SELECT)

for element in cursor.fetchall():
    print(element)


    
connection.commit()

connection.close()

