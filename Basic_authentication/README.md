# API Projects

This repository contains two different API projects: a **Basic Authentication API** and a **Simple User API**. Below are the details for each project.

---

## 1. Basic Authentication API

### Introduction
This project focuses on implementing Basic Authentication for a simple API. The aim is to learn the essentials of the authentication process, such as Base64 encoding, sending authorization headers, and handling authentication and authorization in Flask. While the industry generally uses pre-built frameworks, this project helps you understand the underlying mechanism through hands-on experience.

### Learning Objectives
By the end of this project, you should be able to:
- Understand what authentication is.
- Encode and decode strings using Base64.
- Implement Basic Authentication and send the `Authorization` header.
- Handle authorization errors like `401 Unauthorized` and `403 Forbidden`.
- Build and manage an API authentication system.

### Requirements
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.9).
- Files must end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should conform to pycodestyle standards (version 2.5.*).
- All modules, classes, and functions must include documentation.
- Functions should be type-annotated.
- All files must be executable.

### Practical Tasks

**Task 0:** Simple-basic-API  
Set up a basic API with a single User model and implement methods to serve the API.

**Task 1:** Error Handler: Unauthorized  
Handle `401 Unauthorized` errors by adding an appropriate error handler in the API.

**Task 2:** Error Handler: Forbidden  
Handle `403 Forbidden` errors by adding an appropriate error handler in the API.

**Task 3:** Auth Class  
Create a base `Auth` class to manage API authentication logic, including checking authorization headers and the current user.

**Task 4:** Define Routes That Don't Require Authentication  
Update the `Auth` class to define routes that do not require authentication by excluding specific paths.

**Task 5:** Request Validation  
Validate incoming requests to ensure they have valid authorization headers and access permissions.

**Task 6:** Basic Auth Class  
Create a `BasicAuth` class that inherits from `Auth` to manage Basic Authentication using Base64 encoding.

**Task 7:** Extract Base64  
Implement a method to extract the Base64 part from the `Authorization` header in the Basic Authentication flow.

**Task 8:** Decode Base64  
Add functionality to decode the Base64 string from the `Authorization` header.

**Task 9:** Extract User Credentials  
Extract the user email and password from the decoded Base64 string.

**Task 10:** User Object  
Create logic to match the extracted credentials to a valid user in the database.

**Task 11:** Basic - Overload current_user - and BOOM!
Add the method def current_user(self, request=None) -> TypeVar('User') in the class BasicAuth that overloads Auth and retrieves the User instance for a request.

### Author
[Jesse Brumley](https://github.com/jessebrumley)

---

## 2. Simple User API

### Introduction
This project is a Simple HTTP API that plays with the `User` model. It contains multiple endpoints to manage user data including creating, retrieving, updating, and deleting users.

### Files

#### `models/`
- `base.py`: Base of all models of the API - handles serialization to file.
- `user.py`: User model.

#### `api/v1`
- `app.py`: Entry point of the API.
- `views/index.py`: Basic endpoints of the API: `/status` and `/stats`.
- `views/users.py`: All user-related endpoints.

### Setup

Install the required dependencies by running:

```bash
$ pip3 install -r requirements.txt
```

### Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

### Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
