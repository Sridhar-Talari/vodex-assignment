# FastAPI CRUD Application

This project is a FastAPI application that provides a simple CRUD (Create, Read, Update, Delete) API for managing items with an expiration date. The application connects to a MongoDB database and allows users to perform various operations.

## Table of Contents
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)


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
   │   ├── lib/
   │   │   ├── db.py                 # Database configuration and connection handling
   │   │   └── utils.py              # Utility functions and helper methods
   │   ├── models/
   │   │   ├── clock_in.py           # Pydantic models for clock-in data (request/response validation)
   │   │   └── items.py              # Pydantic models for items data (request/response validation)
   │   ├── routers/
   │   │   ├── clock_in.py           # API routes for clock-in CRUD operations
   │   │   └── items.py              # API routes for items CRUD operations
   │   ├── main.py                   # Entry point for FastAPI application setup
   │
   ├── .venv/                        # Virtual environment for dependencies (excluded from Git)
   ├── .env                          # Environment variables (e.g., database credentials, secret keys)
   ├── .gitignore                    # Specifies files and directories to ignore in Git
   ├── README.md                     # Documentation and project information
   └── requirements.txt              # Project dependencies and packages



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
