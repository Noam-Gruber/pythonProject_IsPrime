# pythonProject_IsPrime
## Overview

This is a simple Python project that checks whether a given number is prime.

## Features

- Accepts user input for a number.
- Checks if the number is prime.
- Displays the result.
- Includes unit tests.
- Integrated with GitHub Actions for Continuous Integration (CI).

## Installation

### Clone the Repository
```
git clone https://github.com/Noam-Gruber/pythonProject_IsPrime.git
cd pythonProject_IsPrime
```

### Install Dependencies
```
pip install -r requirements.txt
```

## Usage
```
python main.py
```

## Running Tests
To run unit tests, execute:
```
python -m unittest discover tests
```

## Continuous Integration (CI)
This project uses GitHub Actions for CI. The workflow:
1. Runs on every push or pull request to main.
2. Checks out the repository.
3. Sets up Python.
4. Installs dependencies.
5. Runs unit tests.
