# Lichess Dashboard 
## Reach-Hub's Assessment | Pranjal Kumar
Assessment files for reach-hub custom Lichess API, featuring Frontend client and Backend server.

## Built with
- **Frontend:** ReactJs, axios, react-hooks, recharts
- **Backend:** Python, FastAPI, PostgreSQL

<img alt="Chess Doodle: pranjal-barnwal" src="https://cdn.dribbble.com/users/872671/screenshots/2751155/linechessset2.gif" width="300"/>

## Functionality
- Access and view the rating history for an individual player
- Obtain list of top-performing players.
- Download a CSV document comprising the complete rating history for all players.

## Endpoints of API
| Endpoint                            | Method | Description                                      | Example                                      |
| ----------------------------------- | ------ | ------------------------------------------------ | -------------------------------------------- |
| `/player/{username}/rating-history`  | GET    | Username's rating history                     | `curl {baseURL}/player/{username}/rating-history` |
| `/top-players`                      | GET    | Returns list of top players                          | `curl {baseURL}/top-players`     |
| `/players/rating-history-csv`        | GET    | Download top players' rating history in CSV         | `curl {baseURL}/players/rating-history-csv` |

- **{baseurl}:** for running API service locally will be: `localhost:8000` by default

## Documentation
- [**Backend Doc**](https://github.com/pranjal-barnwal/reach-hub/blob/main/backend/README.md)
- [**Frontend Doc**](https://github.com/pranjal-barnwal/reach-hub/blob/main/frontend/README.md)

## Requirements
- Git
- PostgreSQL
- Python
- NodeJs
- NPM

## Clone the Repository
```bash
git clone git@github.com:pranjal-barnwal/reach-hub.git
cd reach-hub
```

## Database set up
```bash
```

## Server set up
```bash
# moving to the backend folder
cd .\backend\ 

# installing all the dependencies
pip i

# activating virtual environment script
.\env\Scripts\activate

# running app of main.py for server
uvicorn main:app --reload
```


## Frontend set up
```bash
# moving to frontend folder
cd .\frontend\ 

# installing all required dependencies
npm i

# running frontend client
npm start
```


## Optimizations
- Once the top players are loaded in Frontend client, we will check if the rating history CSV has been loaded. If it hasn't, we will start the process in the background. This will allow the CSV to be downloaded faster when the user clicks the "Download CSV" button.

    - *There's a limit of 1 second in Lichess API for each request. So 50 requests will by-default will take about 50 seconds to process with additional delays* 

- More improved model would be first creating the complete CSV table in advance and storing it into the PostgreSQL Database and fetching it directly from our database, instead of using Lichess API again and again.

    - *We would still need to update the database daily because of updated ratings. So we can use a self repeatable function with 1-day delay to update the database*

- Since loading `/top-players` or `/player/{username}/rating-history` endpoint is not resource and time intensive, so we don't need to store them in Database


## License
[**MIT License**](https://github.com/pranjal-barnwal/reach-hub/blob/main/license)


## Show your support
Hit the ⭐ if you liked this Project!

<img src="https://media.giphy.com/media/mGcNjsfWAjY5AEZNw6/giphy.gif" width="80">