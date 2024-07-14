# Library Management System

## Project Overview
The Library Management System (LMS) is designed to manage and automate the core processes involved in running a small to medium-sized library. 

## Design Decisions
- **Structure**: The system is divided into several modules (`book.py`, `user.py`, `models.py`, `storage.py`, `check.py`), each handling a specific part of the library's operations. This separation of concerns allows for easier maintenance and scalability.
- **Data Models**: The `models.py` file encapsulates the data models, separating the business logic from the data access layers, which simplifies the database interactions and changes to the data schema.
- **Storage Management**: Implemented in `storage.py`, this module handles data persistence, enabling data storage and retrieval operations to be centralized and potentially swapped with different storage solutions without affecting other parts of the system.
- **User and Book Management**: `user.py` and `book.py` are dedicated to managing the interactions related to users and books respectively, providing a clear interface and functions specific to the operations required by these entities.
- **System Checks**: `check.py` includes functions to enforce business rules and constraints, ensuring data integrity and correct system behavior.

## Requirements
- Python 3.8 or higher

## Execution instruction
Just clone the repository, and run main.py

## Usage
To run the system, execute the `main.py` script from the command line.

## Unit Testing
Unit tests are located in the `test` directory. To run all tests, use the following command:
python -m unittest discover -s test

Each test file corresponds to a module in the system, ensuring that each component functions as expected independently.

## Project Directory Structure
- `main.py`: Main executable script that launches the library management system.
- `book.py`: Manages book-related operations such as additions, deletions, and searches within the library system.
- `user.py`: Handles user-related functionalities including user creation, modification, and deletion.
- `models.py`: Defines the data models, representing the structure of the data within the system such as books and users.
- `storage.py`: Responsible for data storage operations, facilitating interactions with the underlying database or storage mechanism.
- `check.py`: Contains utility functions and system checks to ensure the integrity and constraints of the system operations.
- `test/`: Directory containing all unit tests to validate the functionality of each component.

## Test Directory Structure
- `test/`
  - `test_book.py`: Contains unit tests for book-related functionalities in `book.py`.
  - `test_user.py`: Contains unit test verifying user management functions in `user.py`.
  - `test_models.py`: Contains unit test that checks the integrity and functionality of the data models defined in `models.py`.
  - `test_check.py`: Contains unit test that ensure they properly enforce system constraints.

