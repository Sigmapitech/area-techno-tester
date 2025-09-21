# Consideration for SQLAlchemy

## Overview

[SQLAlchemy](https://www.sqlalchemy.org/) is a Python SQL toolkit and Object Relational Mapper (ORM).
It allows developers to interact with databases using Python objects instead of writing raw SQL for every query.
SQLAlchemy supports multiple database engines (like PostgreSQL, MySQL, SQLite) and provides both high-level
ORM features and lower-level core SQL expression tools. For this project we decided to go with MariaDB
as the database backend, but SQLAlchemy makes it possible to switch technologies if needed in the future.

## Why we considered it?

SQLAlchemy is widely used in Python projects for database management. It simplifies repetitive SQL
operations and provides flexibility to switch between different database backends.
Its ORM layer makes it easier to map database tables to Python classes, which can speed up
development when working with complex data models.

## Who in the group has prior knowledge about this tech?

Gabriel and Yohann have experience with SQLAlchemy. The rest of the group has little to no familiarity with it.

## How could this tech allow us to improve our workflow?

* Avoids writing raw SQL for most queries, saving time on common database operations.
* Provides a consistent API across multiple database systems.
* The ORM makes it easier to structure and maintain data models.
* Can integrate smoothly with Python-based backends (like Flask or FastAPI).

## What is the general feeling?

The general feeling is cautiously positive. While SQLAlchemy has a learning curve,
especially for those unfamiliar with Python ORMs, it is a mature and well-documented library
with strong community support. Its flexibility ensures that both simple and complex use cases
can be handled effectively, and team members who already know it can help onboard others.

## Advantages

* Mature, widely adopted, and well-documented.
* Reduces boilerplate SQL by using Python objects.
* Flexible: allows both ORM and direct SQL expressions.
* Supports multiple database engines with minimal code changes.
* Strong integration with modern Python backends and libraries.

## Disadvantages

* Steeper learning curve for those unfamiliar with Python or ORMs.
* Can add complexity compared to writing raw SQL for very simple queries.
* Requires some onboarding for group members new to the tool.

## Use Cases

* Applications with complex data models that benefit from an ORM.
* Python-based projects requiring database integration.
* Projects that may need to switch between different database backends.
* Systems where long-term maintainability and scalability are important.

## Conclusion

SQLAlchemy is a powerful and reliable choice for managing databases in Python projects.
While it may take some effort for the entire team to get comfortable with its abstractions,
the benefits in maintainability, flexibility, and reduced boilerplate are significant.
With Gabriel and Yohann already experienced in SQLAlchemy, the learning curve can be smoothed out for others.
Overall, adopting SQLAlchemy provides a solid foundation for handling database operations in our project,
both now and in the long term.
