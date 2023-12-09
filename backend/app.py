from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Database Configuration (Can be placed in a separate config.py file)
DB_NAME = "Lichess"
DB_USER = "admin"
DB_PASSWORD = "secretpass"
DB_HOST = "localhost"  # or your PostgreSQL host

# Function to establish connection to the database
def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
    )

# Example FastAPI route to fetch and store data in the database
@app.get("/fetch-and-store-data")
def fetch_and_store_data():
    try:
        # Fetch data (Replace this with your logic to fetch data)
        fetched_data = ["example_data_1", "example_data_2"]

        # Establish connection to the database
        conn = get_db_connection()

        # Create a cursor object to execute PostgreSQL commands
        cursor = conn.cursor()

        # Example: Insert fetched data into the database
        for data in fetched_data:
            cursor.execute("INSERT INTO your_table_name (column_name) VALUES (%s)", (data,))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        return {"message": "Data fetched and stored successfully!"}

    except Exception as e:
        return {"error": f"Error occurred: {str(e)}"}
