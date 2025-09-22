# Tech Tester Arena

Welcome to **Tech Tester Arena**!
This project is designed to explore and compare various web technologies.

## Tested Technologies

Tested technologies are split into POC (proof of concept) and Con (Consideration)

- Back:
  - Con - **Express**
  - Con - **Flask**
  - Con - **PHP**
  - POC - **FastAPI**
- DB:
  - Con - **MangoDB**
  - Con - **PostgresSQL**
  - Con - **SQLite**
  - POC - **SQLAlchemy**
- Front:
  - Con - **Angular**
  - Con - **HTML / CSS / JavaScript**
  - Con - **Vue.js**
  - POC - **React**
- Mobile:
  - Con - **Flutter**
  - Con - **Kotlin**
  - Con - **React Native**
  - POC - **React + Capacitor**

## Purpose
Evaluate, prototype, and benchmark multiple frameworks and languages to identify the most suitable technology for the EPITECH arena project. This platform supports learning, experimentation, and informed decision-making.

## Structure

```
tech-tester-arena
├── poc
│   ├── front-react
│   ├── back-fastapi
│   └── db-orm-slqalchemy
└─── considerations
    ├── back-express
    ├── back-fastapi
    ├── back-flask
    ├── back-php
    ├── db-mongo
    ├── db-postgres
    ├── db-sql-alchemy
    ├── db-sqlite
    ├── front-angular
    ├── front-html-css-js
    ├── front-react
    ├── front-vue
    ├── mobile-flutter
    ├── mobile-kotlin
    └── mobile-react-native 
```

## POC / Con testing policy
- Con:
  - Basic oficial tutorial
    - front: routing, components, data store (eg. jwt token)
    - back: routing, json, cron, oauth2
  - Multiple questions to answer:
    - Why we considered it? (short description about it)
    - Who in the group has prior knowledge about this tech?
    - What this tech could allows us to improve our area workflow?
    - What is General feeling? (intallation, tools, libs & support)
- POC:
  - min req for fonctional area project

## Our choices

After testing multiple technologies we decided to settle on these:
 - fastAPI for the backend.
 - SQLAlchemy for the orm.
 - React for the frontend of the web application.
 - React with capacitor for the frontend of the mobile application. 
