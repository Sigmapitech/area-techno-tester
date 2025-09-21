# Consideration for PHP

## Overview
[PHP](https://www.php.net/) is a widely used, general-purpose
scripting language designed for web development.
It runs on the server side and powers a large portion of the internet,
including platforms like WordPress, Drupal, and MediaWiki.
PHP is often embedded directly into HTML,
but can also be used with frameworks (e.g., Laravel, Symfony)
to build more structured and scalable applications.
Its maturity and widespread adoption make it a reliable choice for backend development.

## Why we considered it?
We considered PHP because it allows us to build
and customize our own lightweight framework without
relying on external dependencies. By working directly with raw PHP,
we gain full control over the project structure, routing, and logic.
This approach also helps the team better understand how frameworks
work under the hood, while keeping the solution simple and tailored to our specific needs.

## Who in the group has prior knowledge about this tech?
Yohann have prior experience with PHP, which can help speed up development and troubleshooting.

## How could this tech allow us to improve our area workflow?
- Provide a lightweight and fully customizable backend tailored to our project needs.
- Enable direct control over routing, request handling, and application structure.
- Allow rapid prototyping and iteration thanks to PHP's simple syntax.
- Simplify deployment due to PHP's universal support across hosting environments.
- Large pool of tutorials, guides, and community support makes problem-solving easier.

## What is General feeling? (installation, tools, libs & support)
- **Installation**: PHP comes pre-installed on many web servers.
- **Tools**: With modern tooling (Composer), package management is simple.
- **Libraries & Support**: Very large ecosystem. PHP has been around for decades, with countless libraries and frameworks available.
- **Learning Curve**: Easy to start with but comes with caveats

## Advantages
- Extremely widespread and well-supported on nearly all hosting providers.
- Simple syntax and beginner-friendly learning path.
- Huge ecosystem with mature frameworks and libraries.
- Large, active community with extensive documentation and resources.

## Disadvantages
- Synchronous by default — not optimized for highly concurrent or real-time applications.
- Raw PHP can lead to messy, unstructured code if not carefully managed.
- Some legacy perceptions of PHP being "outdated", despite modern improvements.
- Requires discipline and frameworks for large, maintainable projects.

## Use Cases
- Content management systems (WordPress, Drupal, Joomla).
- Traditional server-rendered web applications.
- REST APIs and backend services with frameworks like Laravel.
- Rapid prototyping for web applications.
- Projects hosted on shared or low-cost hosting providers.

## Test
A simple PHP demonstrating a basic API to provide structured endpoints.

## Conclusion
PHP is a dependable choice for backend development due to its simplicity, broad availability,
and strong ecosystem.
While it may not offer the performance of modern async frameworks like FastAPI,
its ease of use and deployment make it suitable for projects prioritizing accessibility and stability.
For our project, PHP provides a solid backend solution despite lacking some
advanced features of newer technologies.
