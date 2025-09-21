# Consideration for SQLite

## Overview
SQLite is a lightweight, self-contained, serverless SQL database engine.
It stores an entire database in a single file, requires no configuration,
and supports most standard SQL features. SQLite is designed for reliability,
portability, and simplicity, making it ideal for embedded applications,
local storage, and small-to-medium web projects.

## Why we considered it?
We considered SQLite because it provides a simple yet reliable solution for
storing structured data without requiring a separate database server.
Its ease of use and portability make it a good fit for small web applications
or prototypes, and it can be integrated easily with most programming languages
and frameworks used in our project.

## Who in the group had prior knowledge about this tech?
Gabriel and Yohann have prior experience with SQLite, meaning most of the team wouldn't
need to learn it from scratch.

## How could this tech allow us to improve our area workflow?
- Provide a lightweight, zero-configuration database for storing and managing data locally.
- Simplify development and testing by embedding the database directly within the project.
- Enable portable database files that can be easily shared between team members or moved across environments.
- Reduce dependency on external infrastructure or servers, speeding up deployment and prototyping.

## What is General Feeling? (installations, tools, libs & support)
Overall, working with SQLite is straightforward. Installation is minimal—usually
requiring just a library—and documentation is extensive and easy to follow.
Integrations with most programming languages are simple,
making it accessible even for those new to database management.

## Advantages
- Serverless and zero-configuration, reducing setup and maintenance overhead.
- ACID-compliant, reliable, and resistant to crashes or data corruption.
- Lightweight and fast for small to medium datasets.
- Cross-platform and portable as a single-file database.
- Easy to integrate into web, mobile, or desktop applications.

## Disadvantages
- Limited concurrency: only one write can occur at a time.
- Not suitable for large-scale, high-traffic web applications.
- Lacks advanced features such as stored procedures, built-in user management, or replication.
- Write-heavy applications may experience performance bottlenecks.

## Use Cases
- Small web applications or prototypes.
- Embedded applications or mobile apps with local data storage.
- Development and testing environments where simplicity and reliability are priorities.

## Conclusion
SQLite offers a simple and reliable way to manage structured data for our project.
Its ease of integration and minimal setup make it highly suitable for our workflow.
While it is not designed for high-concurrency or large-scale applications,
it fits the needs of our team for lightweight, local, or embedded data storage.