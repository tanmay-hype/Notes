# DBMS vs RDBMS

- **DBMS (Database Management System)**: is a software system that allows users to define, create, maintain, and control access to databases. It can manage various types of databases, including hierarchical, network, and relational databases.
Eg: Examples of DBMS include Microsoft Access, Oracle Berkeley DB, and IBM IMS.
* **RDBMS (Relational Database Management System)**: is a type of DBMS that is based on the relational model. It organizes data into tables (relations) consisting of rows and columns, and it uses Structured Query Language (SQL) for database access and manipulation.
Eg: Examples of RDBMS include MySQL, PostgreSQL, Oracle Database, and Microsoft SQL Server.

### Key Differences between DBMS and RDBMS:
1. **Data Model**: DBMS can handle various data models, while RDBMS specifically uses the relational model.
2. **Data Structure**: In DBMS, data can be structured in different ways (hierarchical, network), whereas in RDBMS, data is organized into tables with rows and columns.
3. **Query Language**: DBMS may use different query languages depending on the type of database, while RDBMS uses SQL as the standard query language.
4. **ACID Properties**: RDBMS typically supports ACID (Atomicity, Consistency, Isolation, Durability) properties more robustly than other types of DBMS.
5. **Scalability**: RDBMS often provide better scalability options for large-scale applications compared to other types of DBMS.

# File System v/s DBMS

- **File System**: A file system is a method of organizing and storing files on a storage device. It provides a way to store, retrieve, and manage files and directories.
Eg : Examples of file systems include NTFS, FAT32, ext4, and HFS+.
- **DBMS**: A Database Management System is a software system that provides an interface for users to interact with databases, allowing for efficient data management, retrieval, and manipulation.
Eg: Examples of DBMS include MySQL, PostgreSQL, Oracle Database, and Microsoft SQL Server.

### Key Differences between File System and DBMS:
1. **Data Storage**: File systems store data in files, while DBMS stores data in structured formats (tables, records).
2. **Data Redundancy**: File systems often lead to data redundancy and inconsistency, while DBMS minimizes redundancy through normalization and relationships.
3. **Data Integrity**: DBMS enforces data integrity constraints, while file systems do not have built-in mechanisms for ensuring data integrity.
4. **Querying**: DBMS allows complex querying and data manipulation using SQL, while file systems typically require custom code for data retrieval and manipulation.
5. **Concurrency Control**: DBMS provides mechanisms for concurrent access and transaction management, while file systems lack such features, leading to potential data conflicts when multiple users access the same file simultaneously.
6. **Security**: DBMS offers advanced security features, including user authentication and access control, while file systems have limited security capabilities, often relying on operating system-level permissions.

# Relational v/s Non-Relational Databases

- **Relational Databases**: These databases are based on the relational model and use tables to store data. Each table consists of rows (records) and columns (attributes), and relationships between tables are established through foreign keys. Relational databases use SQL for querying and managing data.
Eg: Examples of relational databases include MySQL, PostgreSQL, Oracle Database, and Microsoft SQL Server.

- **Non-Relational Databases**: Also known as NoSQL databases, these databases do not follow the relational model. They can store data in various formats, such as key-value pairs, documents, wide-column stores, or graphs. Non-relational databases are designed for scalability and flexibility, often used for handling large volumes of unstructured or semi-structured data.
Eg: Examples of non-relational databases include MongoDB (document store), Redis (key-value store), Cassandra (wide-column store), and Neo4j (graph database).

### Key Differences between Relational and Non-Relational Databases:
1. **Data Model**: Relational databases use a structured table-based model, while non-relational databases use various data models (key-value, document, column-family, graph).
2. **Schema**: Relational databases have a fixed schema, requiring predefined structures for tables, while non-relational databases often have a flexible or dynamic schema, allowing for easier changes to data structures.
3. **Query Language**: Relational databases use SQL for querying, while non-relational databases may use different query languages or APIs specific to their data model (e.g., MongoDB uses a query language based on JSON).
4. **Scalability**: Non-relational databases are generally designed for horizontal scalability, making them suitable for distributed systems and large-scale applications, while relational databases typically scale vertically, which can be more challenging for very large datasets.
5. **Use Cases**: Relational databases are often used for applications requiring complex queries and transactions, such as financial systems, while non-relational databases are preferred for applications with large volumes of unstructured data, real-time analytics, and content management systems.

# DBMS Architecture

- **Three-Tier Architecture**: The three-tier architecture of a DBMS consists of three layers: the presentation layer (user interface), the application layer (business logic), and the data layer (database management). This architecture separates concerns, allowing for better scalability, maintainability, and security.

   1. **Presentation Layer**: This layer is responsible for interacting with the user. It includes the user interface components that allow users to input data and view results. It can be a web interface, desktop application, or mobile app.
     
    -  User interface components that allow users to input data and view results. It can be a web interface, desktop application, or mobile app.
   
   2. **Application Layer**: This layer contains the business logic and application processing. It handles the processing of user requests, applies business rules, and communicates with the data layer to retrieve or update data. It acts as an intermediary between the presentation layer and the data layer.
   -  User requests are processed in this layer, and it ensures that the appropriate actions are taken based on the application's requirements. It may include application servers, APIs, and other components that facilitate communication between the user interface and the database.

   3. **Data Layer**: This layer is responsible for managing the database and handling data storage, retrieval, and manipulation. It includes the DBMS itself, which provides the necessary tools and services for managing the database, ensuring data integrity, and enforcing security measures. The data layer interacts directly with the underlying database and executes SQL queries or other data operations as requested by the application layer.

   - The data layer is crucial for maintaining the overall performance and reliability of the database system. It ensures that data is stored efficiently, retrieved quickly, and remains consistent and secure throughout its lifecycle.

# 3 Schema Architecture of DBMS

- **External Schema (View Level)**: This level defines how users interact with the database. It consists of multiple user views, each tailored to the specific needs of different users or applications. The external schema provides a way to present data in a format that is meaningful and relevant to the end-users, while abstracting away the complexities of the underlying database structure. 
  - Use cases: it allows different users to have customized views of the data, ensuring that they only see the information that is relevant to their roles and responsibilities. 
  - Eg: A sales manager may have a view that shows sales data by region, while a finance analyst may have a view that focuses on revenue and expenses.

- **Conceptual Schema (Logical Level)**: This level represents the overall logical structure of the entire database. It defines the entities, relationships, and constraints that govern the data. The conceptual schema provides a unified view of the data, independent of how it is physically stored, allowing for better data management and integrity.
  - Use cases: it serves as a blueprint for the database design, ensuring that all data is organized in a consistent and coherent manner. It also facilitates communication between database designers, developers, and users by providing a common understanding of the data model.
  - Eg: A conceptual schema might define the relationship between customers, orders, and products in a retail database.

- **Internal Schema (Physical Level)**: This level describes how the data is physically stored in the database. It includes details about data storage structures, indexing methods, and access paths. The internal schema is concerned with optimizing performance and ensuring efficient data retrieval and storage, while remaining transparent to users and applications interacting with the database.
    - Use cases: it allows database administrators to fine-tune the performance of the database by selecting appropriate storage structures and indexing strategies. It also ensures that data is stored in a way that maximizes efficiency and minimizes resource usage.
    - Eg: An internal schema might specify that customer data is stored in a B-tree index for fast retrieval, while order data is stored in a hash table for quick access based on order IDs.

# Data Independence
- **Data Independence**: refers to the ability to change the schema at one level of a database system without affecting the schema at the next higher level. It allows for flexibility in database design and maintenance, enabling changes to be made without disrupting the overall functionality of the system.
### Types of Data Independence:
1. **Logical Data Independence**: This type of data independence allows changes to the conceptual schema (logical level) without affecting the external schema (view level). It enables modifications to the logical structure of the database, such as adding new fields or changing relationships between entities, without requiring changes to the user views or applications that rely on the data. Logical data independence is crucial for adapting to evolving business requirements and ensuring that the database can accommodate new data needs without disrupting existing applications.
   - Use cases: it allows organizations to evolve their data models over time, adding new features or modifying existing ones without impacting the applications that depend on the data. For example, if a company wants to add a new attribute to a customer entity, such as "loyalty program membership," it can do so without affecting the existing views or applications that access customer data.

2. **Physical Data Independence**: This type of data independence allows changes to the internal schema (physical level) without affecting the conceptual schema (logical level). It enables modifications to the physical storage structures, indexing methods, or access paths used to store and retrieve data, without requiring changes to the logical representation of the data. Physical data independence is essential for optimizing performance and adapting to changes in hardware or storage technologies without impacting the logical structure of the database.
   - Use cases: it allows database administrators to optimize the performance of the database by changing storage structures or indexing strategies without affecting the logical representation of the data. For example, if a database administrator decides to switch from a B-tree index to a hash index for faster data retrieval, they can do so without requiring changes to the logical schema or the applications that access the data.

- **Benefits of Data Independence**: 
   - It enhances the flexibility and adaptability of the database system, allowing for easier maintenance and evolution of the database over time.
   - It reduces the impact of changes on applications and user views, minimizing disruptions and ensuring continuity of operations.
   - It enables better performance optimization by allowing changes to physical storage structures without affecting the logical representation of the data.

# SQL categories
SQL (Structured Query Language) is a standard language used for managing and manipulating relational databases. It provides a set of commands and statements that allow users to perform various operations on the data stored in the database. SQL can be categorized into several types based on the functionality they provide:

1. **Data Definition Language (DDL)**: DDL statements are used to define and manage the structure of database objects, such as tables, indexes, and views. Common DDL commands include:
   - `CREATE`: Used to create new database objects (e.g., tables, indexes).
   - `ALTER`: Used to modify the structure of existing database objects.
   - `DROP`: Used to delete database objects from the database.

2. **Data Manipulation Language (DML)**: DML statements are used to manipulate the data stored in the database. Common DML commands include:
   - `SELECT`: Used to retrieve data from one or more tables.
   - `INSERT`: Used to add new records to a table.
   - `UPDATE`: Used to modify existing records in a table.
   - `DELETE`: Used to remove records from a table.

3. **Data Control Language (DCL)**: DCL statements are used to control access to the data in the database. Common DCL commands include:
   - `GRANT`: Used to give users specific privileges on database objects.
   - `REVOKE`: Used to remove previously granted privileges from users.

4. **Transaction Control Language (TCL)**: TCL statements are used to manage transactions in the database. Common TCL commands include:
   - `COMMIT`: Used to save all changes made during the current transaction.
   - `ROLLBACK`: Used to undo changes made during the current transaction.

5. **Data Query Language (DQL)**: DQL statements are used to query the database and retrieve data based on specific criteria. The primary DQL command is:
   - `SELECT`: Used to retrieve data from one or more tables, allowing users to specify conditions, sorting, and grouping of the results.
   - `WHERE`: Used to filter the results of a SELECT statement based on specific conditions.
   - `ORDER BY`: Used to sort the results of a SELECT statement in ascending or descending order.
   - `GROUP BY`: Used to group the results of a SELECT statement by one or more columns.
   - `HAVING`: Used to filter the results of a GROUP BY clause based on specific conditions.
   - `JOIN`: Used to combine rows from two or more tables based on a related column between them.
   - `UNION`: Used to combine the results of two or more SELECT statements into a single result set, eliminating duplicate rows.
   - `INTERSECT`: Used to return only the rows that are common between two or more SELECT statements.
   - `EXCEPT`: Used to return only the rows that are in the first SELECT statement but not in the second.

# SQL Constraints
SQL constraints are rules that are applied to the columns of a table to enforce data integrity and ensure that the data stored in the database adheres to specific requirements. Constraints help maintain the accuracy and reliability of the data by restricting the types of values that can be inserted or updated in a table. Common SQL constraints include:
1. **NOT NULL**: Ensures that a column cannot have a NULL value. It is used to enforce that a value must be provided for the column when inserting or updating records.
2. **UNIQUE**: Ensures that all values in a column are unique across the table. It prevents duplicate values from being inserted into the column, maintaining data integrity.
3. **PRIMARY KEY**: A combination of NOT NULL and UNIQUE constraints. It uniquely identifies each record in a table. A table can have only one primary key, which can consist of one or more columns (composite key).
4. **FOREIGN KEY**: Establishes a relationship between two tables by linking a column in one table to the primary key of another table. It ensures referential integrity, meaning that the value in the foreign key column must exist in the referenced primary key column.
5. **CHECK**: Ensures that the values in a column meet specific conditions or criteria. It allows for the enforcement of custom rules on the data being inserted or updated in the table.

# ER Models
ER (Entity-Relationship) models are used to represent the structure of a database in a visual way. They show the entities in the database, their attributes, and the relationships between them. ER models are useful for designing and understanding the logical structure of a database before implementing it in a specific DBMS.

1. **Entities**: Entities are objects or concepts that can have data stored about them. They can be physical objects (like a person or a product) or abstract concepts (like a course or an event). Each entity is represented as a rectangle in an ER diagram.
2. **Attributes**: Attributes are the properties or characteristics of an entity. They describe the data that can be stored about the entity. Attributes are represented as ovals connected to their respective entities in an ER diagram. For example, a "Student" entity may have attributes like "StudentID," "Name," and "DateOfBirth."
3. **Relationships**: Relationships represent the associations between entities. They show how entities are related to one another in the database. Relationships are represented as diamonds in an ER diagram, with lines connecting them to the related entities. For example, a ""Enrolls" relationship may connect the "Student" entity to the "Course" entity, indicating that students can enroll in courses.
4. **Cardinality**: Cardinality defines the number of instances of one entity that can be associated with instances of another entity in a relationship. It specifies the minimum and maximum number of occurrences of an entity in relation to another entity. Common cardinalities include one-to-one (1:1), one-to-many (1:N), and many-to-many (M:N). Cardinality is often represented using symbols or annotations on the lines connecting entities in an ER diagram.
5. **Primary Key**: A primary key is a unique identifier for each instance of an entity. It ensures that each record in the entity can be uniquely identified and accessed. In an ER diagram, the primary key is often underlined in the attribute list of the entity. For example, "StudentID" may serve as the primary key for the "Student" entity.
6. **Foreign Key**: A foreign key is an attribute in one entity that refers to the primary key of another entity. It establishes a link between the two entities and enforces referential integrity in the database. In an ER diagram, foreign keys are often represented with dashed lines connecting the related entities. For example, a "CourseID" attribute in the "Enrolls" relationship may serve as a foreign key linking to the "Course" entity's primary key.
7. **Weak Entity**: A weak entity is an entity that cannot be uniquely identified by its own attributes alone and relies on a strong entity for its identification. It has a partial key and is typically represented with a double rectangle in an ER diagram. The relationship between a weak entity and its strong entity is represented with a double diamond. For example, an "OrderItem" entity may be a weak entity that depends on the "Order" entity for its identification, as it cannot exist without being associated with a specific order.
8. **Composite Attribute**: A composite attribute is an attribute that can be divided into smaller sub-attributes, each of which holds a specific piece of information. In an ER diagram, composite attributes are represented as ovals connected to their sub-attributes with lines. For example, a "FullName" attribute may be a composite attribute consisting of "FirstName" and "LastName" sub-attributes.
9. **Derived Attribute**: A derived attribute is an attribute whose value can be calculated or derived from other attributes in the database. It is not stored directly in the database but can be computed when needed. In an ER diagram, derived attributes are often represented with dashed ovals. For example, an "Age" attribute may be a derived attribute calculated from the "DateOfBirth" attribute of a "Person" entity.

# Keys 
The concept of keys is fundamental in database design and management. Keys are attributes or sets of attributes that uniquely identify records within a table or establish relationships between tables. They play a crucial role in ensuring data integrity, enforcing uniqueness, and facilitating efficient data retrieval.

1. **Primary Key**: A primary key is a unique identifier for each record in a table. It ensures that no two records can have the same value for the primary key attribute(s). A primary key can consist of a single attribute or a combination of attributes (composite key). It is essential for maintaining data integrity and enabling efficient data retrieval. In an ER diagram, the primary key is often underlined in the attribute list of the entity.
2. **Foreign Key**: A foreign key is an attribute in one table that refers to the primary key of another table. It establishes a relationship between the two tables and enforces referential integrity, ensuring that the value in the foreign key column must exist in the referenced primary key column.
3. **Candidate Key**: A candidate key is an attribute or a set of attributes that can uniquely identify records in a table. A table can have multiple candidate keys, but only one of them can be chosen as the primary key. Candidate keys are essential for identifying potential primary keys and ensuring data uniqueness.
4. **Alternate Key**: An alternate key is a candidate key that was not selected as the primary key. It serves as an alternative unique identifier for records in a table. Alternate keys can be used to enforce uniqueness and provide additional ways to access records in the database.
5. **Composite Key**: A composite key is a primary key that consists of two or more attributes. It is used when a single attribute is not sufficient to uniquely identify records in a table. Composite keys are often used in many-to-many relationships or when the combination of attributes provides a unique identifier for records. In an ER diagram, composite keys are represented by underlining all the attributes that make up the key. 
6. **Super Key**: A super key is an attribute or a set of attributes that can uniquely identify records in a table. It may contain additional attributes beyond what is necessary for uniqueness. All candidate keys are super keys, but not all super keys are candidate keys. Super keys are important for understanding the relationships between attributes and ensuring data integrity.
7. **Unique Key**: A unique key is an attribute or a set of attributes that enforces uniqueness in a table, similar to a primary key. However, unlike a primary key, a unique key can allow NULL values (depending on the database system). Unique keys are used to ensure that no two records have the same value for the specified attribute(s), maintaining data integrity and preventing duplicate entries.
8. **Surrogate Key**: A surrogate key is an artificial or synthetic key that is created to serve as a unique identifier for records in a table. It is typically an auto-incremented integer or a unique identifier (UUID) that has no inherent meaning or relationship to the actual data. Surrogate keys are often used when natural keys are not suitable or when a simple, consistent identifier is needed for database operations.

# Refrential Integrity
- **Referential Integrity**: is a property of relational databases that ensures that relationships between tables remain consistent. It means that if one table (the child table) has a foreign key that references another table (the parent table), the value of the foreign key must either match a primary key value in the parent table or be NULL. This ensures that there are no orphaned records in the child table, maintaining the integrity of the relationships between tables.
### Key Concepts of Referential Integrity:
1. **Foreign Key Constraint**: A foreign key constraint is a rule that enforces referential integrity by ensuring that the value of a foreign key in the child table corresponds to a valid primary key value in the parent table. If a foreign key value does not match any primary key value in the parent table, the database will reject the operation (insert or update) that violates the constraint.
2. **Cascading Actions**: Cascading actions are options that can be defined for foreign key constraints to specify how changes in the parent table should affect the child table. Common cascading actions include:
   - **CASCADE**: If a record in the parent table is deleted or updated, the corresponding records in the child table will also be deleted or updated automatically. This ensures that the relationships remain consistent without leaving orphaned records.
   - **SET NULL**: If a record in the parent table is deleted or updated, the corresponding foreign key values in the child table will be set to NULL. This allows for the removal of the relationship while preserving the child records.
   - **SET DEFAULT**: If a record in the parent table is deleted or updated, the corresponding foreign key values in the child table will be set to a default value specified for the foreign key column. This allows for maintaining a valid relationship while changing the foreign key value.
3. **ON DELETE and ON UPDATE**: These clauses are used to define the behavior of foreign key constraints when a record in the parent table is deleted or updated. They specify the cascading actions that should be taken to maintain referential integrity in the child table. For example, an ON DELETE CASCADE clause would automatically delete related records in the child table when a record in the parent table is deleted, while an ON UPDATE CASCADE clause would automatically update the foreign key values in the child table when the corresponding primary key value in the parent table is updated. 

# SELECT Fundamentals
The SELECT statement is a fundamental SQL command used to retrieve data from one or more tables in a relational database. It allows users to specify the columns they want to retrieve, apply filtering conditions, sort the results, and perform various operations on the data. The SELECT statement is versatile and can be used in combination with other SQL clauses to create complex queries that meet specific data retrieval requirements.
### Basic Syntax of the SELECT Statement:
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
GROUP BY column
HAVING condition
ORDER BY column ASC|DESC;
```
### Key Components of the SELECT Statement:
1. **SELECT Clause**: The SELECT clause specifies the columns that you want to retrieve from the table(s). You can list individual column names, use the asterisk (*) to select all columns, or apply aggregate functions (e.g., COUNT, SUM, AVG) to perform calculations on the data. For example, `SELECT name, age FROM students;` retrieves the "name" and "age" columns from the "students" table.
2. **FROM Clause**: The FROM clause specifies the table(s) from which to retrieve the data. You can specify a single table or use JOIN operations to combine data from multiple tables based on relationships between them. For example, `FROM students` indicates that the data should be retrieved from the "students" table.
3. **WHERE Clause**: The WHERE clause is used to filter the results based on specific conditions. It allows you to specify criteria that the data must meet in order to be included in the result set. You can use comparison operators (e.g., =, <>, >, <), logical operators (e.g., AND, OR, NOT), and pattern matching (e.g., LIKE) to define the conditions. For example, `WHERE age > 18` filters the results   to include only students older than 18.
4. **GROUP BY Clause**: The GROUP BY clause is used to group rows that have the same values in specified columns into summary rows. It is often used with aggregate functions to perform calculations on each group. For example, `GROUP BY department` groups the rows by the "department" column.
5. **HAVING Clause**: The HAVING clause is used to filter groups after the GROUP BY clause has been applied. It is similar to the WHERE clause but is applied to the grouped data. For example, `HAVING COUNT(*) > 5` filters the groups to include only those with more than 5 rows.
6. **ORDER BY Clause**: The ORDER BY clause is used to sort the results in ascending or descending order based on one or more columns. For example, `ORDER BY name ASC` sorts the results by the "name" column in ascending order.

# Null Handling in SQL
In SQL, NULL represents the absence of a value or an unknown value in a database column. It is important to understand how NULL values are handled in SQL, as they can affect query results and data integrity. NULL is not the same as an empty string or a zero value; it indicates that the value is missing or undefined.
### Key Concepts of NULL Handling in SQL:
1. **NULL Comparison**: When comparing NULL values, the result is always unknown (NULL). Therefore, using standard comparison operators (e.g., =, <>, >, <) with NULL will not yield true or false results. Instead, you should use the `IS NULL` or `IS NOT NULL` operators to check for NULL values. For example, `WHERE column_name IS NULL` filters the results to include only rows where the specified column has a NULL value.
2. **NULL in Aggregate Functions**: When using aggregate functions (e.g., COUNT, SUM, AVG), NULL values are typically ignored in the calculations. For example, `COUNT(column_name)` counts only the non-NULL values in the specified column, while `SUM(column_name)` and `AVG(column_name)` also ignore NULL values when performing their calculations.
3. **NULL in Joins**: When performing JOIN operations, NULL values can affect the results of the join. For example, in an INNER JOIN, rows with NULL values in the join columns will not be included in the result set, while in an OUTER JOIN, rows with NULL values may still be included, depending on the type of outer join (LEFT, RIGHT, or FULL).
4. **NULL in Conditional Expressions**: When using conditional expressions (e.g., CASE statements), NULL values can lead to unexpected results if not handled properly. It is important to account for NULL values in your logic to ensure that the desired outcomes are achieved. For example, you can use the   `COALESCE` function to provide a default value for NULL values in conditional expressions. For example, `COALESCE(column_name, 'default_value')` returns the value of `column_name` if it is not NULL; otherwise, it returns 'default_value'.
5. **NULL in Sorting**: When sorting results using the ORDER BY clause, NULL values are typically treated as the lowest possible values and will appear first in ascending order and last in descending order. However, some database systems allow you to specify how NULL values should be sorted using the `NULLS FIRST` or `NULLS LAST` options. For example, `ORDER BY column_name ASC NULLS LAST` sorts the results in ascending order while placing NULL values at the end of the result set.

# Built-in Functions in SQL
SQL provides a variety of built-in functions that can be used to perform calculations, manipulate data, and retrieve specific information from the database. These functions can be categorized into several types based on their functionality:
1. **Aggregate Functions**: Aggregate functions perform calculations on a set of values and return a single value. Common aggregate functions include:
   - `COUNT()`: Returns the number of rows in a specified column or table.
   - `SUM()`: Returns the total sum of a numeric column.
   - `AVG()`: Returns the average value of a numeric column.
   - `MIN()`: Returns the minimum value in a specified column.
   - `MAX()`: Returns the maximum value in a specified column.
2. **String Functions**: String functions are used to manipulate and process string data. Common string functions include:
   - `CONCAT()`: Concatenates two or more strings into a single string.
   - `LENGTH()`: Returns the length of a string.
   - `SUBSTRING()`: Extracts a substring from a string based on specified starting position and length.
   - `UPPER()`: Converts a string to uppercase.
   - `LOWER()`: Converts a string to lowercase.