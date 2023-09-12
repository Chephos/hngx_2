# hngx_2 Django CRUD API
HNGx Stage 2 task:
This is a simple CRUD (Create, Read, Update, Delete) API built using Django and Django Rest Framework (DRF) for managing a "person" resource.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create and Activate a Virtual Environment](#2-create-and-activate-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Apply Migrations](#4-apply-migrations)
  - [5. Run the Server](#5-run-the-server)
- [API Endpoint](#api-endpoints)
- [Usage](#usage)
  - [1. Creating a Person](#1-creating-a-person)
  - [2. Retrieving a Person](#2-retrieving-a-person)
  - [3. Updating a Person](#3-updating-a-person)
  - [4. Deleting a Person](#4-deleting-a-person)
- [Testing](#testing)
- [Known Limitations and Assumptions](#known-limitations-and-assumptions)

## Requirements

Before setting up and running the API, ensure you have the following:

- Python 3.x
- Django
- Django Rest Framework

## Setup

Follow these steps to set up and run the API on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/Chephos/hngx_2.git
cd hngx_
```

### 2. Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python3 -m venv .venv
```

```bash
# Activate the virtual environment
source .venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```
The API should now be running locally at http://localhost:8000/api/.

## API Endpoints
The API provides the following endpoints:
- `Create a Person` - POST /api/
- `Retrieve a Person` - GET /api/<user_id>/
- `Update a Person` - PUT /api/<user_id>/
- `Delete a Person` - DELETE /api/<user_id>/

## Usage
### 1. Creating a Person
To create a person, send a POST request to the `/api/` 

Request:
```json
{
    "name": "John Doe"
}
```
or run the following command in your terminal:
```bash
curl -X POST http://localhost:8000/api/ -d "name=John Doe"
```

### 2. Retrieving a Person
To retrieve a person, send a GET request to the `/api/<user_id>/`

Request:
```bash
curl -X GET http://localhost:8000/api/<user_id>/
```

Response:
```json
{
    "id": 1,
    "name": "John Doe"
}
```

### 3. Updating a Person
To update a person, send a PUT request to the `/api/<user_id>/`

Request:
```json
{
    "name": "Jane Doe"
}
```
or run the following in your terminal:
```bash
curl -X PUT http://localhost:8000/api/<user_id>/ -d "name=Jane Doe"
```

Response:
```json
{
    "id": 1,
    "name": "Jane Doe"
}
```

### 4. Deleting a Person
To delete a person, send a DELETE request to the `/api/<user_id>/`

Request:
```bash
curl -X DELETE http://localhost:8000/api/<user_id>/
```

Response:
```json
{
    "message": "Person successfully cut off, cheers!"
}
```

## Testing
Run:

```bash
python api/tests.py
```


## Known Limitations and Assumptions
- The API does not support pagination.
- The API does not support filtering.
- The API does not support sorting.
- This documentation assumes a local development setup.
- Authentication and authorization mechanisms are not implemented

