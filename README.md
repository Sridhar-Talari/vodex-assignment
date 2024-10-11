# FastAPI CRUD Application

This project is a FastAPI application that provides a simple CRUD (Create, Read, Update, Delete) API for managing items with an expiration date. The application connects to a MongoDB database and allows users to perform various operations on item entities.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)

## Features

- Create items with a name, email, item name, quantity, and expiration date.
- Retrieve all items or a specific item by ID.
- Update an existing item by ID.
- Delete an item by ID.
- Validates expiration date to ensure it is in `YYYY-MM-DD` format.

## Installation

To run this application, ensure you have Python 3.7 or higher installed. Follow the steps below to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vodex-assignment.git
   cd vodex-assignment

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Start the FastAPI server:
   ```bash
    uvicorn app.main:app --reload

## Folder Structure

vodex-assignment/
│
├── app/
│   ├── __init__.py
│   ├── main.py               # Entry point for the FastAPI application
│   ├── routers/
│   │   ├── __init__.py
│   │   └── items.py          # CRUD operations for items
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py           # Pydantic models for request/response
│   └── database.py           # Database connection setup
│
├── requirements.txt          # Project dependencies
└── .env                      # Environment variables (MongoDB connection string)


## API Endpoints

### Items API

| Method | Endpoint                   | Description                                   |
|--------|----------------------------|-----------------------------------------------|
| POST   | `/items/`                  | Create a new item                             |
| GET    | `/items/{item_id}`         | Retrieve a specific item by ID                |
| PUT    | `/items/{item_id}`         | Update an existing item by ID                 |
| DELETE | `/items/{item_id}`         | Delete an item by ID                          |
| GET    | `/items/filter`            | Filter items based on query parameters         |
| GET    | `/items/aggregate`         | Retrieve aggregated data for items           |

### Clock-In API

| Method | Endpoint                     | Description                                   |
|--------|------------------------------|-----------------------------------------------|
| POST   | `/clock-in/`                 | Create a new clock-in record                 |
| GET    | `/clock-in/{clockin_id}`      | Retrieve a specific clock-in record by ID     |
| PUT    | `/clock-in/{clockin_id}`      | Update an existing clock-in record by ID      |
| DELETE | `/clock-in/{clockin_id}`      | Delete a clock-in record by ID               |
| GET    | `/clock-in/filter`            | Filter clock-in records based on query parameters |



## Conclusion

This FastAPI application allows users to manage items and clock-in records efficiently. Use the provided API documentation to explore and interact with the available endpoints.
