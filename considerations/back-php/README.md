# Consideration for PHP

## Overview
[PHP](https://www.php.net/) is a widely used, general-purpose scripting language designed for web development. It runs on the server side and powers a large portion of the internet, including platforms like WordPress, Drupal, and MediaWiki. PHP is often embedded directly into HTML, but can also be used with frameworks (e.g., Laravel, Symfony) to build more structured and scalable applications. Its maturity and widespread adoption make it a reliable choice for backend development.

## Why we considered it?
We considered PHP because of its long-standing role in web development, ease of deployment, and availability across virtually all hosting platforms.
Our project requires a backend to handle requests and serve dynamic content, and PHP provides a straightforward way to achieve this, especially when paired with a framework like Laravel. Its wide availability and established ecosystem reduce infrastructure complexity, and its syntax is beginner-friendly.

## Who in the group has prior knowledge about this tech?
Yohann have prior experience with PHP, which can help speed up development and troubleshooting.

## How could this tech allow us to improve our area workflow?
- Provide a simple and accessible backend solution for serving dynamic content.
- Enable integration with popular frameworks (Laravel, Symfony) for structured APIs.
- Allow rapid development thanks to PHP’s simple syntax and large library ecosystem.
- Broad hosting support means deployment is straightforward.
- Large pool of tutorials, guides, and community support makes problem-solving easier.

## What is General feeling? (installation, tools, libs & support)
- **Installation**: PHP comes pre-installed on many web servers. With modern tooling (Composer), package management is simple.
- **Tools**: Works well with frameworks like Laravel and Symfony, which provide routing, ORM, and templating out of the box.
- **Libraries & Support**: Very large ecosystem. PHP has been around for decades, with countless libraries and frameworks available.
- **Learning Curve**: Easy to start with. Using raw PHP is simple; mastering frameworks like Laravel requires more time.

## Advantages
- Extremely widespread and well-supported on nearly all hosting providers.
- Simple syntax and beginner-friendly learning path.
- Huge ecosystem with mature frameworks and libraries.
- Large, active community with extensive documentation and resources.
- Laravel (a leading PHP framework) offers modern tools such as routing, authentication, and ORM.

## Disadvantages
- Synchronous by default — not optimized for highly concurrent or real-time applications.
- Raw PHP can lead to messy, unstructured code if not carefully managed.
- Performance is generally lower compared to modern async frameworks like FastAPI.
- Some legacy perceptions of PHP being “outdated,” despite modern improvements.
- Requires discipline and frameworks for large, maintainable projects.

## Use Cases
- Content management systems (WordPress, Drupal, Joomla).
- Traditional server-rendered web applications.
- REST APIs and backend services with frameworks like Laravel.
- Rapid prototyping for web applications.
- Projects hosted on shared or low-cost hosting providers.

## Test
A simple PHP demonstrating a basic REST API to provide structured endpoints.

## Conclusion
PHP is a dependable choice for backend development due to its simplicity, broad availability, and strong ecosystem.
While it may not offer the performance of modern async frameworks like FastAPI, its ease of use and deployment make it suitable for projects prioritizing accessibility and stability.
For our project, PHP provides a solid backend solution despite lacking some advanced features of newer technologies.
