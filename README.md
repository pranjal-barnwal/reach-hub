# Lichess Dashboard | Reach-Hub's Assessment | Pranjal Kumar
Assessment files for reach-hub custom Lichess API

<img alt="Chess Doodle: pranjal-barnwal" src="https://cdn.dribbble.com/users/872671/screenshots/2751155/linechessset2.gif" width="300"/>

## Functionality
- Access and view the rating history for an individual player
- Obtain list of top-performing players.
- Download a CSV document comprising the complete rating history for all players.

## Endpoints of API
| Endpoint                            | Method | Description                                      | Example                                      |
| ----------------------------------- | ------ | ------------------------------------------------ | -------------------------------------------- |
| `/player/{username}/rating-history`  | GET    | Username's rating history                     | `curl {baseURL}/player/johndoe/rating-history` |
| `/top-players`                      | GET    | Returns list of top players                          | `curl {baseURL}/top-players`     |
| `/players/rating-history-csv`        | GET    | Download top players' rating history in CSV         | `curl {baseURL}/players/rating-history-csv` |


## Clone the Repository
```bash
git clone git@github.com:pranjal-barnwal/reach-hub.git
cd reach-hub
```

## Documentation
- [**Backend Doc**](https://github.com/pranjal-barnwal/reach-hub/blob/main/backend/README.md)
- [**Frontend Doc**](https://github.com/pranjal-barnwal/reach-hub/blob/main/frontend/README.md)


## License
[**MIT License**](https://github.com/pranjal-barnwal/reach-hub/blob/main/license)


## Show your support
Hit the ⭐ if you liked this Project!

<img src="https://media.giphy.com/media/mGcNjsfWAjY5AEZNw6/giphy.gif" width="80">