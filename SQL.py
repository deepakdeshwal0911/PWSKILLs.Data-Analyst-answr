"""
Here's each question answered individually:
1) What does SQL stand for?
SQL stands for Structured Query Language — it's the standard language used to communicate with and manage relational databases.
2) List any three common data types used in SQL.
Three common SQL data types are: INT (for whole numbers), VARCHAR(n) (for variable-length text strings), and DATE (for calendar dates). Other common ones include DECIMAL/FLOAT (for numbers with decimals), BOOLEAN, and TEXT.
3) Write a SQL query to fetch all columns from a table named 'users'.
sqlSELECT * FROM users;
4) Explain the difference between WHERE and HAVING clause in SQL.
WHERE filters individual rows before any grouping or aggregation happens, and it cannot reference aggregate functions like SUM or COUNT. HAVING filters groups after aggregation (typically used with GROUP BY), and it's specifically designed to filter based on aggregate results — for example, showing only departments where SUM(Salary) > 100000.
5) What is a primary key in SQL and why is it used?
A primary key is a column (or combination of columns) that uniquely identifies each row in a table — it cannot contain NULL values and must be unique across all rows. It's used to enforce data integrity, prevent duplicate records, and serve as the reference point for foreign key relationships between tables.
6) Write a SQL query to calculate the total number of orders in a table named 'orders'.
sqlSELECT COUNT(*) AS total_orders FROM orders;
7) Explain the concept of SQL injection and how can it be prevented?
SQL injection is a security vulnerability where an attacker inserts malicious SQL code into an input field (like a login form) to manipulate or gain unauthorized access to a database — for example, entering ' OR '1'='1 to bypass authentication. It can be prevented by using parameterized queries (prepared statements) instead of directly concatenating user input into SQL strings, validating and sanitizing all user inputs, applying the principle of least privilege to database accounts, and using ORM frameworks that handle query building safely by default.
8) What is the difference between UNION and UNION ALL in SQL?
UNION combines the result sets of two or more SELECT statements and removes duplicate rows, which requires an internal sorting/comparison step. UNION ALL combines result sets without removing duplicates, making it faster since it skips the deduplication step — it's the better choice when you know there won't be duplicates or when duplicates are acceptable/expected.
9) Discuss the importance of indexes in SQL.
Indexes are special data structures that speed up data retrieval by allowing the database to find rows without scanning the entire table — similar to a book's index letting you jump straight to a topic instead of reading every page. They significantly improve query performance for SELECT, WHERE, JOIN, and ORDER BY operations, but they come with tradeoffs: indexes take up additional storage and can slow down INSERT, UPDATE, and DELETE operations since the index itself must be updated alongside the table data, so they should be applied thoughtfully to frequently queried columns rather than indiscriminately.
10) Write a SQL query to find the second highest salary from an 'employees' table.
sqlSELECT MAX(Salary) AS SecondHighestSalary
FROM employees
WHERE Salary < (SELECT MAX(Salary) FROM employees);
(Alternative using OFFSET/FETCH or DENSE_RANK() also works depending on the SQL dialect, e.g.: SELECT DISTINCT Salary FROM employees ORDER BY Salary DESC OFFSET 1 ROW FETCH NEXT 1 ROW ONLY;)
11) What are the different types of SQL joins?
The main types are: INNER JOIN (returns only matching rows from both tables), LEFT JOIN / LEFT OUTER JOIN (returns all rows from the left table plus matched rows from the right, with NULLs where there's no match), RIGHT JOIN / RIGHT OUTER JOIN (the mirror opposite of LEFT JOIN), FULL JOIN / FULL OUTER JOIN (returns all rows from both tables, matched where possible), and CROSS JOIN (returns the Cartesian product — every row from one table combined with every row from the other).
12) Explain the concept of normalization in SQL.
Normalization is the process of organizing a database's tables and columns to minimize data redundancy and improve data integrity, typically done by splitting large tables into smaller, related ones and defining relationships between them via foreign keys. It's implemented in progressive stages called normal forms (1NF, 2NF, 3NF, and beyond), each addressing specific types of redundancy or dependency issues — for example, 1NF requires atomic column values, while 3NF eliminates transitive dependencies between non-key columns.
13) What is the purpose of the GROUP BY clause in SQL?
GROUP BY groups rows that share the same values in specified columns into summary rows, typically used alongside aggregate functions like SUM, COUNT, AVG, MIN, or MAX — for example, SELECT Department, SUM(Salary) FROM Employees GROUP BY Department; calculates total salary per department rather than per individual row.
14) Write a SQL query to update the 'status' column to 'completed' for all rows in a table named 'tasks'.
sqlUPDATE tasks
SET status = 'completed';
(Note: without a WHERE clause, this updates every row in the table — add a WHERE condition if you only want to update specific rows.)
15) Describe the difference between DELETE and TRUNCATE commands in SQL.
DELETE removes rows from a table one at a time (optionally with a WHERE clause to target specific rows), logs each row deletion individually, can be rolled back within a transaction, and triggers any associated DELETE triggers. TRUNCATE removes all rows from a table at once, is generally much faster since it doesn't log individual row deletions, resets any auto-increment counters, cannot be selectively filtered with a WHERE clause, and in most database systems is harder or impossible to roll back once committed.
"""