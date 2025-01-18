
# Basic Flask Web Application

A simple Flask-based web application that demonstrates user authentication and displays employee details. This project connects to a MySQL database to manage user and employee data.



## Features

-User authentication (login functionality).

-Display employee details based on their role (e.g., Web Developer)

-Separate pages for index, login, and displaying personal details.


## Tech Stack

**Backend:** Python (Flask framework)

**Frontend:** HTML, CSS, Jinja2 templates

**Database:** MySQL (using **pymysql** for connection)

## Prerequisites

Before running this project, ensure you have the following installed:

Python 3.x

MySQL server

Required Python libraries (see requirements.txt)





## Installation

    1. Clone the repository:

        git clone https://github.com/your-username/your-repository.git
        cd your-repository

    2. Install dependencies:

        Ensure you have python installed along with the requird libraries

        -Install Flask and pymysql

        pip install flask pymysql

        -Install MySQL connector for Python

        pip install mysql-connector-python

    3. Set up the MySQL database:

        -Create a database named flasdb.

        -Create the required tables:

        CREATE TABLE user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL
        );

        CREATE TABLE e_detail (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            roll VARCHAR(50),
            salary FLOAT,
            email VARCHAR(100),
            phone_number VARCHAR(15)
        );

    4. Update the database credentials in app.py:

        connection = pymysql.connect(
            host='localhost',
            user='your-username',
            password='your-password',
            database='flasdb',
            port=3306
        )

    4. Run the application:

        python app.py

    5. Open your browser and visit:

        http://127.0.0.1:5000/
        

## Screenshots

### 1. Log In Page

![Screenshot 2025-01-18 203351](https://github.com/user-attachments/assets/4dc8cdbe-89df-4c91-b9a5-f9ac93c27c7c)

### 2. Home page

![Screenshot 2025-01-18 203406](https://github.com/user-attachments/assets/6b8cc6d8-05a6-4569-8ef8-5c26e551f36e)

### 3. Webdevelopers Data

![Screenshot 2025-01-18 203415](https://github.com/user-attachments/assets/d9b9f618-aed0-4ca9-8e66-e6fb7c60a6c0)


