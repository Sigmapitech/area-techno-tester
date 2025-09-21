# Consideration for Flask

## Overview
[Flask](https://flask.palletsprojects.com/) is a lightweight and flexible Python web framework based on WSGI (Web Server Gateway Interface). It follows a "micro" philosophy, providing only the essentials to get an application running, while leaving developers free to choose additional tools and libraries. Flask is known for its simplicity, readability, and large ecosystem of extensions, making it one of the most popular Python web frameworks.

## Why we considered it?
We considered Flask because it provides a minimal, easy-to-use framework for building web applications and APIs.
Our project requires a backend service, and Flask's simplicity allows us to quickly prototype and deliver endpoints without the complexity of larger frameworks. It integrates well with databases, authentication libraries, and templating engines, giving us freedom to build only what we need.
Flask also has a long track record, which means strong community support and a wealth of resources for troubleshooting.

## Who in the group has prior knowledge about this tech?
Yohann has prior experience with Flask, and Flask's simplicity extensive documentation could help get up to speed quickly.

## How could this tech allow us to improve our area workflow?
- Provide a straightforward way to build RESTful APIs.
- Allow rapid prototyping with minimal boilerplate.
- Enable integration with a wide range of Flask extensions (ORMs, authentication, security).
- Offer a flexible foundation where we can pick the best tools for our needs instead of being locked into conventions.
- Good choice for smaller projects or parts of the system that don't require high concurrency.

## What is General feeling? (installation, tools, libs & support)
- **Installation**: Very lightweight - installable via pip. Easy to get a server running in a few lines of code.
- **Tools**: Works well with Jinja2 templating, SQLAlchemy, and extensions for authentication, security, and forms.
- **Libraries & Support**: Huge ecosystem of extensions. Extensive documentation and tutorials due to its maturity.
- **Learning Curve**: Extremely beginner-friendly. Most developers can get started within minutes.

## Advantages
- Simple and minimal - you only use what you need.
- Mature and battle-tested framework with a huge ecosystem of plugins.
- Very beginner-friendly and widely taught, lowering the learning curve.
- Excellent for small to medium projects or quick prototypes.
- Large community with many tutorials, guides, and examples.

## Disadvantages
- Synchronous by default - less efficient for handling very high concurrency compared to FastAPI.
- Requires more manual setup for features like validation, authentication, and async support.
- Can become harder to manage as projects scale, since structure is left up to developers.
- Fewer "modern" conveniences (e.g., auto-generated docs, type safety) compared to newer frameworks like FastAPI.

## Use Cases
- Small to medium web applications.
- RESTful APIs with moderate traffic.
- Prototypes or MVPs that may later be migrated to larger frameworks.
- Educational projects or beginner-friendly setups.
- Services where flexibility and simplicity are more important than raw performance.

## Test
A backend API with a few routes defined in Flask, serving JSON responses.
Basic integration with SQLAlchemy for database persistence.
Demonstration of template rendering with Jinja2 for serving HTML pages alongside APIs.

## Conclusion
Flask is a solid choice for building lightweight APIs and web applications.
It is minimal, flexible, and has a large ecosystem of extensions, making it suitable for rapid development and smaller-scale projects.
However, compared to newer frameworks like FastAPI, it lacks built-in async support, type safety, and automatic documentation.
For our area project, Flask could work well if we prioritize simplicity, but it may require additional setup for features that FastAPI provides out of the box.
