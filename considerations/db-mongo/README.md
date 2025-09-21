# Consideration for MongoDB

## Overview
[MongoDB](https://www.mongodb.com/) is a popular NoSQL database that stores
data in a flexible, JSON-like format. Unlike relational databases, MongoDB uses
collections and documents instead of tables and rows, making it well-suited
for unstructured or rapidly changing data. It is widely adopted for projects
requiring scalability and schema flexibility.

## Why we considered it?
We considered MongoDB because our project may involve storing dynamic or
evolving data structures. MongoDB’s schema-less design allows quick iteration
without heavy database migrations. It also integrates well with Python
libraries (e.g., Motor, PyMongo) and can scale horizontally when needed.

## Who in the group has prior knowledge about this tech?
Yohann has some experience with MongoDB, which could reduce the setup time for
the group.

## How could this tech allow us to improve our area workflow?
- Store JSON-like data directly, simplifying backend integration.
- Reduce database migrations when models change.
- Provide good support for scalability and high-throughput applications.
- Work smoothly with FastAPI through existing libraries.

## What is General feeling? (installation, tools, libs & support)
- **Installation**: Heavier than relational databases; requires running a
  MongoDB service or using a managed option like Atlas.
- **Tools**: MongoDB Compass provides a GUI for managing data.
- **Libraries & Support**: Good Python driver support (PyMongo, Motor).
  Strong ecosystem, though less standardized than SQL-based tools.
- **Learning Curve**: Fairly easy to start, but handling indexes,
  relationships, and schema design needs extra care.

## Advantages
- Flexible, schema-less document storage.
- Good for rapidly evolving data models.
- Scales horizontally with sharding support.
- Widely used, with solid documentation and community resources.

## Disadvantages
- Not as strong for complex queries compared to SQL databases.
- Requires careful schema design to avoid performance issues.
- Joins and relationships are more limited, sometimes leading to data
  duplication.
- Higher resource usage compared to lightweight relational setups.

## Use Cases
- Applications with flexible or unstructured data.
- Rapid prototyping where schema may change often.
- Logging, analytics, or IoT data ingestion.
- Projects expecting horizontal scaling.

## Test
A simple collection storing user documents with JSON-like fields.
Basic insertions operations tested using PyMongo. Retrieval & demo of the
workflow graph with graphviz.

## Conclusion
MongoDB offers flexibility and scalability, making it useful when dealing with
evolving or unstructured data. However, it comes with trade-offs in query
complexity, performance tuning, and schema management. For our project, MongoDB
can be a good fit if we prioritize flexible data storage, though it may require
more care in design compared to traditional relational databases.
