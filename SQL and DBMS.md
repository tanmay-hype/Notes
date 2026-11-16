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

# SQL Constraints
SQL constraints are rules that are applied to the columns of a table to enforce data integrity and ensure that the data stored in the database adheres to specific requirements. Constraints help maintain the accuracy and reliability of the data by restricting the types of values that can be inserted or updated in a table. Common SQL constraints include:
1. **NOT NULL**: Ensures that a column cannot have a NULL value. It is used to enforce that a value must be provided for the column when inserting or updating records.
2. **UNIQUE**: Ensures that all values in a column are unique across the table. It prevents duplicate values from being inserted into the column, maintaining data integrity.
3. **PRIMARY KEY**: A combination of NOT NULL and UNIQUE constraints. It uniquely identifies each record in a table. A table can have only one primary key, which can consist of one or more columns (composite key).
4. **FOREIGN KEY**: Establishes a relationship between two tables by linking a column in one table to the primary key of another table. It ensures referential integrity, meaning that the value in the foreign key column must exist in the referenced primary key column.
5. **CHECK**: Ensures that the values in a column meet specific conditions or criteria. It allows for the enforcement of custom rules on the data being inserted or updated in the table.
