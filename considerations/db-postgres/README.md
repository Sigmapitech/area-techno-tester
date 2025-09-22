# Consideration for PostgreSQL

## Overview
[PostgreSQL](https://www.postgresql.org/) is a powerful, open-source relational database management system (RDBMS) known for its reliability, feature set, and standards compliance. It supports advanced data types, extensibility, and strong ACID compliance, making it a leading choice for applications requiring robust data storage and querying.

## Why we considered it?
PostgreSQL is one of the most widely adopted open-source databases, offering excellent scalability, data integrity, and compatibility with modern web technologies. Its strong support for relational data modeling and advanced querying capabilities makes it well-suited for our project's structured data needs.

## Who in the group has prior knowledge about this tech?
Louis and Lilian has prior experience working with PostgreSQL, while others have used SQL in general, which should ease the learning curve.

## How could this tech allow us to improve our area workflow?
- Provides a reliable and scalable solution for persisting and querying structured data.
- Advanced features such as JSONB support allow mixing relational and semi-structured data without requiring a separate NoSQL database.
- Rich indexing options and query optimization tools help maintain performance as the dataset grows.
- Integration with ORMs and query builders (e.g., Sequelize, SQLAlchemy, Prisma) streamlines backend development with Express.js, fastapi or similar frameworks.
- Strong community and tooling (pgAdmin, psql) simplify database management, monitoring, and migrations.

## What is General feeling? (installation, tools, libs & support)
The general feeling is positive: installation is straightforward across platforms  throught docker, and popular cloud providers offer managed PostgreSQL services.
Tooling (e.g., pgAdmin, DBeaver, Prisma) is mature and widely used.
The community is large, active, and well-documented, so troubleshooting and learning resources are abundant.

## Advantages
- **Reliability**: Proven stability and robust transaction support (ACID compliance).
- **Features**: Advanced data types (JSONB, arrays, GIS), stored procedures, triggers, and full-text search.
- **Performance**: Strong optimization, indexing options, and query planner for large datasets.
- **Extensibility**: Highly customizable with extensions (e.g., PostGIS, pgcrypto).
- **Community**: Strong ecosystem and active development.

## Disadvantages
- **Complexity**: Advanced features and optimization may have a steep learning curve.
- **Setup overhead**: Requires more configuration and management than lightweight alternatives like SQLite.
- **Scaling writes**: Vertical scaling is strong, but horizontal scaling (sharding) is less straightforward compared to some NoSQL solutions.

## Use Cases
- Storing and querying relational data
- Applications requiring strict data integrity and reliability
- APIs or services needing complex queries and analytics
- Systems requiring both relational and JSON-based data handling

## Conclusion
PostgreSQL is a strong candidate for our project due to its reliability, versatility, and robust feature set. While it may introduce a learning curve and require careful setup, its long-term benefits for scalability, data integrity, and performance make it a solid foundation for our area workflow.
