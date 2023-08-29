# 🔊 SHIFTproject

Test task for the course

Python

## Requirements

 - [Python 3.10+](https://www.python.org/)
 - [PostgreSQL](https://www.postgresql.org/download/)

## How to use

1. Change content `.env` in root:
   ```dotenv
   # You will need to install PostgreSQL.
   #Create a local server, and change the settings in the .env folder to yours
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=bd
    DB_USER=postgres
    DB_PASS=postgres
   ```

2. Creation
   ```
   To create a virtual environment, go to your project directory and run: python -m venv .venv
   Activate the virtual environment:
   venv\Scripts\activate.bat
   - for Windows;
   source venv/bin/activate
   - for Linux and MacOS.
   
   install the libraries we need from the requirements file (you can find it inside the project)
   ```

3. Run server/migration
   ```shell
   $ alembic init migrations # After creating a local network, you need to make migrations to your database
   $ alembic revision --autogenerate -m "yourName" # create a revision
   $ alembic upgrade head # save/update our database
   ```

4. After everything is ready, we can start our server!.
   ```shell
   $ python -m uvicorn main:app --reload # start the server
   $ http://127.0.0.1:8000/docs#/ # Use this address to work with the project
   ```
   **https://fastapi.tiangolo.com/features/** For more information, please refer to the documentation

---

- **License:** © 2023 Vud18.<br>