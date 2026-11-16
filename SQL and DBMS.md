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