# Custom Lichess Backend with FastAPI & PostgreSQL
by **ReachHub** | [**Pranjal Kumar**](https://linkedin.com/in/pranjal-barnwal)

# Index
- [Requirements](#requirements)
- [Database set up](#database-set-up)
- [Server Set up](#server-set-up)
- [main.py](#mainpy)
  - [Summary](#summary)
  - [Modules and Dependencies](#modules-and-dependencies)
  - [FastAPI Configuration](#fastapi-configuration)
  - [Endpoints](#endpoints)
- [app.py](#apppy)
  - [Summary](#summary-1)
  - [Dependencies](#dependencies)
  - [Database Connection](#database-connection)
  - [Functions](#functions)
  - [Usage](#usage)
- [Sample Data](#sample-data)
  - [Top Players Data](#top-players-data)
  - [Rating History for player](#rating-history-for-player)
  - [Rating History CSV](#rating-history-csv)

## Requirements
- PostgreSQL
- Python


## Database set up
1. Install [**PostgreSQL**](https://www.postgresql.org/download/) with default configurations
1. Set `username` and `password`, remember this because we will need it in `./backend/app.py` file to connect with database
1. Open **pgAdmin** client
1. Create Database with name: `csvstore`
1. Inside `csvstore`, create Table with name: `csvtable`
1. Inside `csvtable`, create Column: `csv_content`. 
1. With this our schema is ready
1. Now come back to: `./backend/app.py` file and update all the necessary changes, updating the credentials into it
    ```py
    conn = psycopg2.connect(
        dbname='csvstore',
        user='postgres',
        password='1234',
        host='localhost',
        port="5432"
    )
    ```
1. Now we're ready to move forward

## Server Set up
```bash
# moving to the backend folder
cd .\backend\ 

# installing all the dependencies
pip i fastapi requests io csv datetime psycopg2

# activating virtual environment script
.\env\Scripts\activate

# running app of main.py for server
uvicorn main:app --reload
```

## main.py
### Summary
This code demonstrates the integration of Reach-Hub's custom Lichess API with FastAPI's Backend server and provides a Frontend client setup.

### Modules and Dependencies
- `FastAPI`: Used for creating the Backend server.
- `requests`: Handles API requests to the Lichess API.
- `StringIO`: Provides an in-memory file-like object for CSV handling.
- `csv`: Manages CSV file operations.
- `datetime`, `timedelta`: Supports time-based operations.

### FastAPI Configuration
The code initializes a FastAPI instance and configures CORS settings for local development.

### Endpoints

1. **Home Endpoint (`"/"`)**
   - Displays a welcome message and links to API documentation.

2. **Top Players Endpoint (`"/top-players"`)**
   - Fetches data for the top 50 classical chess players from the Lichess API.

3. **Rating History Endpoint (`"/player/{username}/rating-history"`)**
   - Retrieves the 30-day rating history for a specified player from the Lichess API.

4. **Rating History CSV Endpoint (`"/players/rating-history-csv"`)**
   - Generates and provides a CSV file of the top 50 players' rating history.
   - Checks if the data is already present in the PostgreSQL Database. If so, fetches and returns it.
   - If not present, fetches player data from the Lichess API, processes it into a CSV, saves it to the database, and returns the CSV data as a response.

### Database Interaction

- `checkDataPresent()`: Checks if data exists in the PostgreSQL Database.
- `saveCsv(csv_content)`: Saves CSV content to the PostgreSQL Database.
- `fetchCsv()`: Fetches CSV content from the PostgreSQL Database.

### Usage

- Start the FastAPI server to handle API requests and interact with the Lichess API and PostgreSQL Database.

For detailed usage and setup, refer to the linked GitHub repository in the code.


## app.py
#### Summary
This code snippet interacts with a PostgreSQL database to perform operations like saving, checking data presence, and fetching CSV content.

#### Dependencies
The code utilizes the `psycopg2` library to establish a connection and interact with the PostgreSQL database.

#### Database Connection

- `conn`: Establishes a connection to the PostgreSQL database with specified credentials (dbname, user, password, host, port).

#### Functions

##### `saveCsv(csv_content)`

- Saves CSV content into the 'csvtable' in the connected PostgreSQL database.
  - Opens a cursor to perform database operations.
  - Executes an SQL command to insert the CSV content into the 'csvtable'.
  - Commits changes and closes the connection after insertion.

##### `checkDataPresent()`

- Checks data presence in the 'csvtable' of the connected PostgreSQL database.
  - Opens a cursor to perform database operations.
  - Executes an SQL command to count rows in the 'csvtable'.
  - Fetches the result and determines data presence based on the count.
  - Returns `True` if data is present; otherwise, returns `False`.

##### `fetchCsv()`

- Fetches CSV content from the 'csvtable' of the connected PostgreSQL database.
  - Opens a cursor to perform database operations.
  - Executes an SQL command to select the CSV content from the 'csvtable'.
  - Fetches the CSV content from the query result assuming there's only one row.
  - Commits changes and closes the connection after fetching.

#### Usage

- Establish a PostgreSQL database connection before invoking functions.
- `saveCsv(csv_content)`: To save CSV content into the 'csvtable'.
- `checkDataPresent()`: To check data presence in the 'csvtable'.
- `fetchCsv()`: To fetch CSV content from the 'csvtable'.

For detailed understanding, refer to the code comments and make sure to handle exceptions appropriately in a production environment.



## Sample Data
- [Top Player Data](#top-players-data)
- [Rating History for player](#rating-history-for-player)
- [Rating History CSV](#rating-history-csv)
---

### Top Players Data
This endpoint returns array of top players details. Each including: **[`id`,`username`,`rating`]**
> **Reference:** https://lichess.org/api/player/top/50/classical

**Endpoint:** `/top-players`

#### Sample Output
```json
{
  "top_players": [
    ["apodex64", "Apodex64", 2555],
    ["unkreativ3", "Unkreativ3", 2535],
    ["josip_buje", "Josip_buje", 2534],
    ...
  ]
}
```
---





### Rating History for player
This Endpoint will return last 30 dates ratings for the mentioned user. Each row including: **[`date`, `rating`]**
> **Reference:** https://lichess.org/api/user/{username}/rating-history/classical

For dates where no-rating is mentioned, we copied the last available data.

**Endpoint:** `/player/{username}/rating-history`

#### Sample Output
```json
{
  "points": [
    ["09-11-2023", 2102],
    ["10-11-2023", 2102],
    ["11-11-2023", 2350],
    ...
  ]
}
```
---



### Rating History CSV
This Endpoint will generate CSV file of last 30 days rating of top 50 players
It internally uses function call of Rating History of Player repetitively for Top 50 players following: ***Do not repeat principle***

**Endpoint:** `/players/rating-history-csv`

#### Sample Output
```csv
username,09-11-2023,10-11-2023,11-11-2023,12-11-2023,13-11-2023,14-11-2023,15-11-2023,...
Apodex64,0,2532,2544,2544,2544,2544,2544,...
Unkreativ3,0,0,0,0,2522,2522,2522,...
Josip_buje,0,0,0,0,0,2533,2533,...
OjaiJoao,2479,2481,2481,2481,2481,2481,2481,...
igormezentsev,0,2472,2469,2469,2470,2476,2479,...
DrOrfeo,0,0,2429,2429,2429,2429,2429,...
...
```
---


