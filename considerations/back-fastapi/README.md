# Consideration for FastAPI

## Overview
[FastAPI](https://fastapi.tiangolo.com/) is a modern, high-performance web framework for building APIs with Python. FastAPI emphasizes speed, developer productivity, and type safety, making it one of the most widely adopted Python web frameworks today. It fully supports asynchronous programming (ASGI), allowing applications to handle large volumes of concurrent requests efficiently.

## Why we considered it?
We considered FastAPI because it combines performance, ease of development, and robustness.
Our project requires a backend capable of handling API requests, data validation, and potential scalability to support real-time or high-throughput workloads. FastAPI offers all of these out of the box, with minimal boilerplate and strong typing. Additionally, its integration with Pydantic ensures reliable request/response validation, while its ecosystem supports databases (e.g., SQLAlchemy) and authentication.
Because several members already have experience with FastAPI, adopting it reduces onboarding time and speeds up development.

## Who in the group has prior knowledge about this tech?
Gabriel, Yohann and Julien have prior experience with FastAPI, making it easier for the group to adopt.

## How could this tech allow us to improve our area workflow?
- Provide a clean and fast way to build backend APIs that integrate with our frontend.
- Enforce type safety and schema validation automatically through Pydantic.
- Support asynchronous endpoints, allowing efficient handling of multiple requests.
- Simplify authentication and security handling via dependency injection.
- Offer built-in interactive API documentation (Swagger UI and ReDoc), improving both development and presentation.
- Enable rapid prototyping while remaining production-ready.

## What is General feeling? (installation, tools, libs & support)
- **Installation**: Very lightweight — installable via pip. Runs with Uvicorn or Hypercorn for ASGI servers.
- **Tools**: Excellent built-in developer tools, including auto-generated docs. Easy to integrate with SQLAlchemy, Alembic, and other Python ecosystem tools.
- **Libraries & Support**: Large and growing ecosystem. Very active community and strong documentation.
- **Learning Curve**: Easy to pick up, especially for those familiar with Python. More advanced async features and security models may require extra learning.

## Advantages
- Extremely fast performance due to ASGI and async support.
- Automatic request/response validation with Pydantic.
- Auto-generated API documentation (Swagger/ReDoc) out of the box.
- Strong typing improves reliability and maintainability.
- Good integration with databases, authentication systems, and background tasks.
- Large and growing community with extensive documentation and tutorials.

## Disadvantages
- Relatively new compared to older Python frameworks like Django or Flask, meaning fewer long-term battle-tested plugins.
- Async programming can be tricky to master for beginners.
- CSRF protection for form submissions must be handled manually.
- Some advanced database integrations (e.g., async SQLAlchemy) require careful configuration.

## Use Cases
- RESTful APIs for web or mobile applications.
- Real-time services (chat, notifications, IoT APIs).
- Data processing or machine learning model serving.
- Lightweight microservices in larger architectures.
- Any project requiring robust and efficient backend APIs.

## Test
A backend API serving JSON responses, validated through Pydantic models.
Endpoints include CRUD operations, authentication, and protected routes.
Interactive API docs (Swagger UI) demonstrate live request/response examples.

## Conclusion
FastAPI is a strong backend choice for our project, offering speed, developer productivity, and reliability. Its combination of async support, schema validation, and interactive documentation makes it highly suitable for building modern APIs. While some security configurations (e.g., CSRF for forms) require additional setup, its advantages outweigh the drawbacks. Given the group’s prior experience, FastAPI provides an efficient and future-proof foundation for the backend of our area project.
