<!-- TOC -->
* [PostgreSQL Questions](#postgresql-questions)
  * [What is a non-clustered index?](#what-is-a-non-clustered-index)
  * [Can you store binary data in PostgreSQL?](#can-you-store-binary-data-in-postgresql)
  * [Explain functions in PostgreSQL](#explain-functions-in-postgresql)
  * [How can we change the column data type in SQL?](#how-can-we-change-the-column-data-type-in-sql)
  * [Explain Write-Ahead Logging](#explain-write-ahead-logging)
  * [What is multi-version concurrency control in PostgreSQL?](#what-is-multi-version-concurrency-control-in-postgresql)
  * [What do you understand by a partitioned table in PostgreSQL?](#what-do-you-understand-by-a-partitioned-table-in-postgresql)
  * [What are the Indices of PostgreSQL?](#what-are-the-indices-of-postgresql)
  * [What is the use of indexes in PostgreSQL?](#what-is-the-use-of-indexes-in-postgresql)
  * [What do we call database callback functions? What is its purpose?](#what-do-we-call-database-callback-functions-what-is-its-purpose)
  * [What does a Cluster index do?](#what-does-a-cluster-index-do)
  * [What are the different properties of a transaction in PostgreSQL?](#what-are-the-different-properties-of-a-transaction-in-postgresql)
  * [Which commands are used to control transactions in PostgreSQL?](#which-commands-are-used-to-control-transactions-in-postgresql)
  * [The Write-Ahead Logging](#the-write-ahead-logging)
  * [What are the three phenomena that must be prevented between concurrent transactions in PostgreSQL?](#what-are-the-three-phenomena-that-must-be-prevented-between-concurrent-transactions-in-postgresql)
<!-- TOC -->

# PostgreSQL Questions

## What is a non-clustered index?

A non-clustered index is a type of index where the order of the rows does not match the order of the actual data.

## Can you store binary data in PostgreSQL?

There are two ways to store the binary data in PostgreSQL, either by using bytes or the large object feature.

## Explain functions in PostgreSQL

Functions in PostgreSQL are also known as stored procedures. They are used to store commands, declarations, assignments,
etc. This makes it easy to perform operations that would generally take thousands of lines of code to write.

PostgreSQL functions can be created in several languages such as SQL, PL/pgSQL, C, Python, etc.

## How can we change the column data type in SQL?

Column data types in PostgreSQL are changed using the ALTER TABLE statement combined with the ALTER COLUMN statement.

## Explain Write-Ahead Logging

This feature provides a log of a database in case of a database crash by logging changes before any changes or updates
are made to the database.

## What is multi-version concurrency control in PostgreSQL?

It is a method commonly used to provide concurrent access to the database, and in programming languages to implement
transactional memory. It avoids unnecessary locking of the database - removing the time lag for the user to log into the
database.

## What do you understand by a partitioned table in PostgreSQL?

In PostgreSQL, a partitioned table is a logical structure used to split a large table into smaller pieces. These small
pieces of the tables are called partitions.

## What are the Indices of PostgreSQL?

Indices of PostgreSQL are inbuilt functions or methods such as GIST Indices, hash table, and B-tree (Binary tree). The
user uses these to scan the index in a backward manner. PostgreSQL also facilitates their users to define their indices
of PostgreSQL.

## What is the use of indexes in PostgreSQL?

In PostgreSQL, indexes are used by the search engine to enhance the speed of data retrieval.

## What do we call database callback functions? What is its purpose?

The database callback functions are known as PostgreSQL Triggers. The PostgreSQL Triggers are performed or invoked
automatically whenever a specified database event occurs.

## What does a Cluster index do?

A Cluster index is used to sort table data rows according to their key values.

## What are the different properties of a transaction in PostgreSQL?

PostgreSQL supports ACID properties. This is commonly referred to by the acronym named ACID. It means the properties of
a transaction in PostgreSQL include Atomicity, Consistency, Isolation, and Durability.

## Which commands are used to control transactions in PostgreSQL?

The following commands are used to control transactions in PostgreSQL:

`BEGIN TRANSACTION`

`COMMIT`

`ROLLBACK`

## The Write-Ahead Logging

The Write-Ahead Logging feature is used to enhance the reliability of the database by logging changes before any changes
or updating to the database. It provides the database log in case of a database failure and ensures to start the work
again from the point it was crashed or discontinued.

## What are the three phenomena that must be prevented between concurrent transactions in PostgreSQL?

There are four levels of transaction isolation used in SQL standard regarding three phenomena that must be prevented
between concurrent transactions in PostgreSQL. These three unwanted phenomena are as follows:

- Dirty read: A transaction is called a dirty read when it reads data written by a concurrent uncommitted transaction.
- Non-repeatable read: It specifies a transaction that re-reads the data it has previously read and then finds another
  transaction that has already modified it.
- Phantom read: It specifies a transaction that re-executes a query, returning a set of rows that satisfy a search
  condition and then finds that the set of rows satisfying the condition has changed due to another recently-committed
  transaction.
