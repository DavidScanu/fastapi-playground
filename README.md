# Playground FastAPI + PostgreSQL

## 1. Créer un stack

- Frontend : 
- Backend : FastAPI ✔️
- Base de données : PostgreSQL ✔️
- pgAdmin 4 ✔️

## 🏃 Usage

The provided instructions detail the steps for setting up and running the application with a **PostgreSQL** database using **Docker Compose**.

### 1. Set PostgreSQL database environment variables

Before running `docker compose up`, you will need to create a `.env` file at the root level, in which you should provide the following PostgreSQL database information: database name, username, and password.

```
POSTGRES_DB=backend_db
POSTGRES_USER=testuser
POSTGRES_PASSWORD=testpwd
```

*Note: The `.env` file should not be versioned and should be added to your `.gitignore` file.*


### 2. Run the application

```
docker compose up
```

## Ressources : 

- https://fastapi.tiangolo.com/tutorial/sql-databases/
- https://devopswithdocker.com/
- https://sqlmodel.tiangolo.com/#sql-databases-in-fastapi
- https://stackoverflow.com/questions/75192148/fastapi-and-postgresql-in-docker-compose-file-connection-error
- https://www.pgadmin.org/docs/pgadmin4/latest/index.html