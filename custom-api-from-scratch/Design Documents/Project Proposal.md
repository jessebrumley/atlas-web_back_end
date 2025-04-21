# 🎵 Music Genre API – Project Proposal

## 🎯 Project Overview

**Project Name**: Music Genre API

**Objective**: Develop a RESTful API that provides information about music genres, artists, albums, and songs. This project serves as a learning exercise to understand API development.

**Scope**: To implement endpoints to retrieve details about genres, artists, albums, and songs. I will focus on creating a minimum viable product without a user interface.

**Target Audience**: While the API is not intended for a specific audience, a complete product would cater to developers, music enthusiasts, and educational institutions.

---

## ✅ Functional Requirements

1. **GET /genres**: Retrieve a list of all music genres.
2. **GET /genres/{id}**: Retrieve a genre by its numeric ID.
3. **GET /genres/{name}**: Retrieve a genre by its name (case-insensitive).
4. **GET /artists**: Retrieve a list of all artists.
5. **GET /artists/{id}**: Retrieve an artist by ID.
6. **GET /artists/{name}**: Retrieve an artist by its name.
7. **GET /albums**: Retrieve a list of all albums.
8. **GET /albums/{id}**: Retrieve an album by ID.
9. **GET /albums/{name}**: Retrieve an album by its name.
10. **GET /songs**: Retrieve a list of all songs.
11. **GET /songs/{id}**: Retrieve a song by ID.
12. **GET /songs/{name}**: Retrieve a song by its name.

---

## ⚙️ Non-Functional Requirements

- **Performance**: Ensure quick API responses with minimal latency.
- **Scalability**: Design the system to handle an increasing number of requests.
- **Maintainability**: Write clean, well-documented, and modular code to facilitate future enhancements.

---

## 🛠️ Tools and Technologies

- **Backend Framework**: Express.js
- **Runtime Environment**: Node.js
- **Data Source**: JSON file (`data.json`) obtained and formatted using Python from the Deezer Music API.
- **API Documentation**: Swagger with `swagger-jsdoc` and `swagger-ui-express`.
- **Logging**: `winston` for robust logging capabilities.
- **Testing**: `mocha`, `chai`, and `supertest` for unit and integration testing.
- **Version Control**: Git

---

## 🧱 Data Model

The data is structured in a nested JSON format as follows:

- genres:
  - id: int
  - name: str
  - artists:
    - id: int
    - name: str
    - albums:
      - id: int
      - title: str
      - release_year: str
      - songs:
        - id: int
        - title: str
        - duration: int
        - preview: str

---

## 📅 Development Timeline

| Phase                    | Duration  | Description                                        |
|--------------------------|-----------|----------------------------------------------------|
| Planning & Data Prep     | 4 days    | Define project scope, obtain and format data.       |
| Implementation           | 10 days   | Develop API endpoints and integrate with data.     |
| Testing & Documentation  | 3 days    | Write tests and generate API documentation.        |
| Optional Features        | as time allows | Implement additional features like pagination, authentication, etc. |

---

## 🚀 Planned Features

As per the project requirements, the following features are planned:

- **Logging**: Implement logging using `winston` to monitor API requests and errors.
- **Unit Testing**: Write unit tests using `mocha`, `chai`, and `supertest` to ensure API reliability.
- **API Documentation**: Auto-generate API documentation using Swagger with `swagger-jsdoc` and `swagger-ui-express`.
- **Pagination**: Modify API endpoints to support pagination for large datasets.
- **Optional Enhancements**: If time permits, implement user authentication, caching mechanisms, queuing systems, and WebSocket support.

---

## 🔒 Assumptions and Constraints

- The API is a learning project and not intended for production use.
- Data is static and stored in a JSON file.
- No user interface will be developed as part of this project.
- The project is developed individually without external collaboration.

## 👤 Developer

**Jesse Brumley**  
GitHub: [https://github.com/jessebrumley](https://github.com/jessebrumley)  
Email: [jesse.brumley@atlasschool.com](mailto:jesse.brumley@atlasschool.com)