# Library Management System

## Project Description

The Library Management System is a Python CLI application used to manage book records. It allows users to add books, display available books, and store book details in a CSV file.

## Project Objectives

- Organize the application using reusable Python modules.
- Validate user inputs.
- Store and load book records using CSV.
- Handle common file errors.
- Record application events using logging.
- Test application functionality using pytest.

## Features

- Add new books.
- Display available books.
- Save book records in a CSV file.
- Load saved books when the application restarts.
- Validate empty inputs.
- Prevent duplicate book IDs.
- Log application activities and errors.
- Handle missing or invalid CSV data.
- Run automated tests using pytest.

## Project Structure

- book.py — Book class.
- library.py — Library operations, validation, CSV handling, and logging.
- main.py — Main CLI application.
- test_library.py — Automated tests.
- books.csv — Saved book records.
- library.log — Application activity log.

## Technologies Used

- Python 3.12 or later
- CSV
- Logging
- Pytest

## Requirements

- Python 3.12 or later
- Pytest installed in the active Python environment

Install pytest if required:

bash
python -m pip install pytest


## Run the Application

Open a terminal in the project directory and run:

bash
python main.py


## Run Tests

Run the automated tests with:

bash
pytest -v


The latest recorded test run completed with 5 passed tests.

## Input Validation and Error Handling

The application checks for empty book details and duplicate book IDs. It also handles common file and CSV errors and records important events in the log file.

## Team Responsibilities

- *Thamzid Hussain Shaik Gaffar:* Modules, packages, and dependency setup.
- *Bhuvaneswari Galam:* Exception handling, file handling, and input validation.
- *Thupakula Divya:* Pytest coverage, integration, and final demo.

## Future Enhancements

- Search books by ID, title, or author.
- Update and delete book records.
- Add book issue and return functionality.
- Improve test coverage and add more features.

## Conclusion

This project demonstrates Python modules, object-oriented programming, CSV file handling, input validation, logging, and automated testing in a simple Library Management System.