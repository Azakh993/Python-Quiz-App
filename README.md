# Python Quiz App
Welcome to the Python Quiz App; my first Python based project! This web-based application allows users to participate in quizzes on various topics. 

## Overview
The Python Quiz App follows a layered architecture pattern to ensure separation of concerns and maintainability. Here's an overview of each layer:

- **Controllers:** Responsible for handling HTTP requests, invoking services, and returning appropriate responses. Includes separate controllers for dashboard, login, and quiz functionalities.

- **Services:** Contains business logic for various features such as authentication, dashboard management, and quiz functionalities. Services communicate with repositories to perform CRUD operations on data.

- **Repositories:** Handles data persistence and retrieval operations. Each repository is responsible for interacting with a specific data entity (e.g., user, quiz, question).

- **Models:** Defines data models used throughout the application. Models represent database tables and are used by repositories for data manipulation.

- **Configuration:** Contains configuration files, including database configurations.

- **Static and Templates:** Includes static assets like CSS files and HTML templates used for rendering views.
