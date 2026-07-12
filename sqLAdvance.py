"""
1) What is the purpose of the SQL LIKE operator?
The LIKE operator is used in a WHERE clause to search for a specified pattern within a text column, rather than requiring an exact match. It's commonly used for partial string matching — for example, finding all customer names that start with "A" or contain a specific substring — using wildcard characters to define the pattern.
2) How is the COUNT function used in SQL? Provide an example.
COUNT returns the number of rows that match a specified condition. For example:
sqlSELECT COUNT(*) AS total_customers FROM customers;
This returns the total number of rows in the customers table. You can also use COUNT(column_name) to count only non-NULL values in a specific column, or COUNT(DISTINCT column_name) to count unique values.
3) Explain the difference between WHERE clause and HAVING clause in SQL.
WHERE filters individual rows before any grouping or aggregation occurs, and it cannot reference aggregate functions. HAVING filters after aggregation, typically used alongside GROUP BY, and is specifically meant to filter based on aggregate results — for example, HAVING SUM(Sales) > 10000 to show only groups whose total exceeds a threshold.
4) What are aggregate functions in SQL? Provide examples of at least three aggregate functions.
Aggregate functions perform a calculation across multiple rows and return a single summarized value. Common examples include:

SUM() — adds up all values in a column
AVG() — calculates the average of values in a column
COUNT() — counts the number of rows
(Others include MIN(), MAX())

5) Write a SQL query to find the average salary of employees in each department using the AVG function.
sqlSELECT Department, AVG(Salary) AS AverageSalary
FROM employees
GROUP BY Department;
6) Discuss the importance of GROUP BY clause in SQL queries with examples.
GROUP BY is essential for summarizing data at a categorical level rather than viewing every individual row — it groups rows sharing the same value in one or more columns so aggregate functions can be applied per group. For example:
sqlSELECT Region, SUM(Sales) AS TotalSales
FROM orders
GROUP BY Region;
This returns total sales per region instead of a single grand total, making it foundational for reporting and dashboard-style summaries (e.g., sales by category, headcount by department, average order value by customer segment).
7) How does the SQL LIKE operator work with wildcards? Provide examples.
LIKE uses two main wildcard characters: % (matches zero or more characters) and _ (matches exactly one character). Examples:
sqlSELECT * FROM customers WHERE Name LIKE 'A%';     -- Names starting with "A"
SELECT * FROM customers WHERE Name LIKE '%son';    -- Names ending with "son"
SELECT * FROM customers WHERE Name LIKE '%an%';    -- Names containing "an" anywhere
SELECT * FROM customers WHERE Name LIKE '_ohn';    -- Matches "John", "Bohn", etc. (single character wildcard)
8) Explain the concept of DISTINCT keyword in SQL with an example.
DISTINCT removes duplicate values from the result set, returning only unique rows or unique combinations of the selected columns. For example:
sqlSELECT DISTINCT Department FROM employees;
This returns each department name only once, even if many employees share the same department.
9) What is the purpose of the SQL MAX function? How is it different from the MIN function?
MAX() returns the largest value in a specified column, while MIN() returns the smallest value in that column. For example, SELECT MAX(Salary) FROM employees; returns the highest salary, whereas SELECT MIN(Salary) FROM employees; returns the lowest — both are useful for quickly identifying the range or extremes within a dataset.
10) Compare and contrast the functions SUM() and AVG() in SQL.
SUM() adds up all values in a column to produce a total, while AVG() calculates the mean by dividing that same total by the number of values. Both are aggregate functions typically used with GROUP BY, but they answer different questions — SUM tells you the overall magnitude (e.g., total revenue), while AVG tells you the typical or central value (e.g., average order size), and the two can give very different impressions of the same dataset, especially when it includes outliers or an uneven number of records per group.
11) Write a SQL query to find the total number of orders placed by each customer using COUNT() and GROUP BY.
sqlSELECT CustomerID, COUNT(*) AS TotalOrders
FROM orders
GROUP BY CustomerID;
12) How can the SQL LIKE operator be used in combination with other operators to filter data effectively?
LIKE can be combined with logical operators like AND, OR, and NOT to build more precise filters. For example:
sqlSELECT * FROM employees
WHERE Name LIKE 'J%' AND Department = 'Sales';
This finds employees whose name starts with "J" and who work in the Sales department. Similarly, NOT LIKE can exclude a pattern (e.g., WHERE Email NOT LIKE '%@test.com' to exclude test accounts), and multiple LIKE conditions can be chained with OR to match several possible patterns at once, such as WHERE ProductName LIKE '%Phone%' OR ProductName LIKE '%Tablet%'."""