# Technical Analysis Report

## Introduction

The **Area** is an automation platform, similar to [IFTTT](https://ifttt.com/) or [Zapier](https://zapier.com/),
which enables users to connect different services, letting an event in one automatically trigger a reaction in another.
It consists of three main parts: a server that runs the core logic, a web app where users can access and
manage their automations, and a mobile app that offers the same functionality on the go. Together, these
components provide a simple and flexible way for users to create and control automated workflows across multiple services.


In order to realize the project, we considered multiple technologies, and thus decided to test them.
We listed each of them in the considerations folder, each having their own sub-folders. For every consideration
we would create a branch for it, and do a basic tutorial for said consideration. While we would do the tutorial,
every person would note some information about the technologie they’re testing, such as how the language felt
as a whole or how it could help us upgrade our workflow. Once all that was done, we would create a markdown
file for said technologies that would answer all questions and include other information such as the language
utility or who in our group had knowledge about this. Once all that was done, we would create a pull request,
and ask for at leIn order to realize the project, we considered multiple technologies, and thus decided to test them. We listed each of them in the considerations folder, each having their own sub-folders. For every consideration we would create a branch for it, and do a basic tutorial for said consideration. While we would do the tutorial, every person would note some information about the technologie they’re testing, such as how the language felt as a whole or how it could help us upgrade our workflow. Once all that was done, we would create a markdown file for said technologies that would answer all questions and include other information such as the language utility or who in our group had knowledge about this. Once all that was done, we would create a pull request, and ask for at least two persons to review it. They would try the considerations and if it reached what was expected, it would be merged towards the main.
Once that was done, we selected the technologies we preferred and made a POC with them. The POC included a connection page, an OAuth connection and an application that uses the OAuth connection.ast one persons to review it. They would try the considerations and if it reached what was
expected, it would be merged towards the main.

Once that was done, we selected the technologies we preferred and made a POC with them.
The POC included a connection page, an OAuth connection and an application that uses the OAuth connection.


## Frontend technologies

For our frontend technologies, we will expand more on [React](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/front-react), [Vue](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/front-vue) and [Angular](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/front-angular).

Of all the frameworks we tried, React is the one where our group has the most experience. While Angular and
React are as complete as each other, our additional knowledge of the latter will make for a smoother development.
It is to be noted that while slightly harder than Vue, it retains its compatibility with capacitor and our
overall higher with it means that the difference is only relative. Thus, we decided to lean towards React as
the frontend for our web application.

## Backend technologies

For our backtend technologies, we will expand more on [fastAPI](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/back-fastapi), [Express](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/back-express) and [Flask](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/back-flask).

When it comes down to the backend, we let ourselves the choice between Express, Flask and FastAPI. Off the
three we decided to go with FastAPI due to speed, the fact that it’s adapted to most API and our good experience with it.
It is also more structured than Express and less limited than Flask.


## Mobile technologies

For our backtend technologies, we will expand more on [React + capacitor](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/front-react), [Flutter](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/mobile-flutter) and [Kotlin](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/mobile-kotlin).

In the end our choice went to React combined with capacitor. While it doesn’t have the power of Flutter,
nor the official label of Kotlin; our superior knowledge of it is a decent point in its favor.
On top of that, the fact that it is React means that it will have a good synergy with our web frontend and
will potentially allow us to share some components. Additionally, the ease of installation is a very good point
for the different environment our team possesses.


## Databases

For our backtend technologies, we will expand more on [MangoDB](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/db-mongo), [SQLAlchemy](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/db-sqlalchemy) and [SQLite](https://github.com/Sigmapitech/area-techno-tester/tree/main/considerations/db-sqlite).

For our database, we decided to lean towards SQLAlchemy. To begin with, it offers a better resilience
than MangoDB, a very important factor for a database. We chose it over SQLite due to its scalability,
making it better at creating bigger apps. 

## Security audit

## Conclusion

