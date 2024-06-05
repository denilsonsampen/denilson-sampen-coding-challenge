# Denilson Sampen - Globant Data Engineering Coding Challenge
This repository contains my solution for the Globant Data Engineering Coding Challenge. The solutions are implemented using Python.

## Table of Contents
- [About the project](#about-the-project)
- [Technologies Used](#technologies-used)
- [Libraries Used](#libraries-used)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [Testing](#testing)

## About the Project
This project shows my solutions for the Globant Data Engineering Coding Challenge. It includes Python scripts for data engineering processes.

## Technologies Used
- Python

## Libraries Used
Detailed in requirements.txt
- pandas
- flask
- sqlalchemy
- requests

## Folder Structure
```
denilson-sampen-coding-challenge/
│
├── api/ # Contains API related code
├── data/ # Contains data files
├── db/ # Contains database related files
├── test/ # Contains test cases
├── utils/ # Contains utility scripts
├── .gitignore
└── README.md
└── requirements.txt
```

## Setup Instructions
1. Clone the repository:
```sh
git clone https://github.com/denilsonsampen/denilson-sampen-coding-challenge.git
```
2. Navigate to the project directory:
```sh
cd denilson-sampen-coding-challenge
```
3. Install the required dependencies:
```sh
pip install -r requirements.txt
```
4. Set up the SQLAlchemy DB
```sh
cd db
python db_creation.py
```

## Testing
1. Run the Flask application (from the denilson-sampen-coding-challenge folder)
```sh
cd api
flask run
```

2. In a new terminal, to Test Section 1: API
```sh
cd test
python test_post.py
```
3. To Test Section 2: SQL
For the first requirement
```sh
cd test
python test_get_1.py
```

For the second requirement
```sh
cd test
python test_get_2.py
```