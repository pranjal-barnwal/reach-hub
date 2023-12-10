import psycopg2

# Establish connection to your PostgreSQL database
conn = psycopg2.connect(
    dbname='csvstore',
    user='postgres',
    password='1234',
    host='localhost',
    port="5432"
)


def saveCsv(csv_content):
    # print("SAVE CSV")
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute an SQL command to insert the CSV content into the database
    cur.execute("INSERT INTO csvtable (csv_content) VALUES (%s)", (csv_content,))

    # Commit changes and close the connection
    conn.commit()
    cur.close()

def checkDataPresent():
    # print("CHECK DATA PRESENT")
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute an SQL command to select the CSV content from the database
    cur.execute("SELECT COUNT(*) FROM csvtable")

    # Fetch the result after executing the query
    result = cur.fetchone()
    cnt = result[0] if result is not None else None

    cur.close()
    print(cnt)

    if cnt is 0:
        return False
    else:
        return True

def fetchCsv():
    # print("FETCH CSV")
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute an SQL command to select the CSV content from the database
    cur.execute("SELECT csv_content FROM csvtable")  # Add your WHERE clause as needed

    # Fetch the result (CSV content) from the query
    csv_content = cur.fetchone()[0]  # Assuming there's only one row with the CSV content

    # Commit changes and close the connection
    conn.commit()
    cur.close()

    # Now csv_content variable holds the retrieved CSV content as a string
    return csv_content
