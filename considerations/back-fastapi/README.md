# Fastapi

Fast API is a python powered framework that allow to create ASGI (Asynchronous
Server Gateway Interface) web server. It offers very high performance and
minimal boilerplate out of the box increasing the speed to develop any
application with it. It is easy to learn thanks to a great documentation and
has been adopted by many, making it one of the most goto technology in python
today.

One of FastAPI’s key strengths is its asynchronous support, which allows
handling many concurrent requests efficiently, making it suitable for
applications with high throughput or real-time features, that need to scale. It
also had first class support with `pydantic` to validate json schema and orm
such as `SQLAchemy`.

We considered `fastapi` because multiple member of our group had prior
experience with it (Gabriel, Yohann) and we already knew it would be a great
choice to build our backend with.

It also has built-in tools to declare security dependencies for endpoints, and
protection against common web vulnerabilities. It has to be noted, however,
that we will need to handle CSRF protection ourselves when creating forms, and
ensure proper configuration for the security to remain strong.
