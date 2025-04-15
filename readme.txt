# FastAPI with PostgreSQL in Docker - Setup Guide


## Prerequisites
Ensure the following are installed on your system:
- Docker and Docker Compose (Install from https://docs.docker.com/get-docker/)
- Python 3.9 or later (Download from https://www.python.org/downloads/)
- Postman (Optional, for API testing)


## Project Structure
```
project/
├── app/
│   ├── main.py            # FastAPI application
│   ├── models.py          # SQLAlchemy models
│   ├── database.py        # Database connection
│   ├── api/               # API routes
│   ├── schemas.py         # Pydantic schemas
│   ├── utils/             # Utility functions
├── Dockerfile             # Dockerfile for FastAPI
├── docker-compose.yml     # Docker Compose setup
├── requirements.txt       # Dependencies
└── README.md              # Setup instructions
```


## Step 1: Clone the Repository
Run the following commands to clone the repository and navigate into the project directory:
```bash
git clone https://github.com/your-repo/fastapi-postgres-docker.git
cd fastapi-postgres-docker
```


## Step 2: Set Up Docker and PostgreSQL


### Start PostgreSQL and FastAPI in Docker
Run the following command to build and start the services:
```bash
docker-compose up --build
```
This will start PostgreSQL on port 5432 and FastAPI on port 8000.


### Check Running Containers
To verify that PostgreSQL and FastAPI containers are running, execute:
```bash
docker ps
```


## Step 3: Access PostgreSQL Inside Docker


### Connect to PostgreSQL in the Running Container
```bash
docker exec -it my_postgres_container psql -U postgres
```
To connect to a specific database, run:
```bash
psql -U postgres -d mydatabase
```


### List Databases
```sql
\l
```


### Connect to a Database
```sql
\c mydatabase
```


### Exit the PostgreSQL Shell
```sql
\q
```


## Step 4: Set Up FastAPI


### Install Dependencies (If Not Using Docker)
If running FastAPI without Docker, install dependencies manually:
```bash
pip install -r requirements.txt
```


### Run FastAPI Locally
Execute the following command:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```


## Step 5: Test the API Using Postman


### Open API Documentation
Visit http://localhost:8000/docs to explore the FastAPI interactive docs.


### Create a User (POST /users/)
#### Request Body:
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "test123"
}
```
#### Curl Command:
```bash
curl -X 'POST' \
  'http://localhost:8000/users/' \
  -H 'Content-Type: application/json' \
  -d '{ "username": "testuser", "email": "test@example.com", "password": "test123" }'
```


### Create a Code File (POST /codes/)
#### Request Body:
```json
{
    "filename": "example.py",
    "content": "def add(a, b):\n    return a + b",
    "language": "python"
}
```


### Retrieve a Code File (GET /codes/{id})
```bash
curl -X 'GET' 'http://localhost:8000/codes/1'
```


## Step 6: Stopping and Restarting Docker Containers


### Stop Running Containers
```bash
docker-compose down
```


### Restart Containers
```bash
docker-compose up -d
```


## Troubleshooting


### Check Docker Logs
```bash
docker logs my_postgres_container
```


### If Unable to Connect to PostgreSQL
- Ensure the container is running: `docker ps`
- Restart the container: `docker-compose restart`
- Check logs: `docker logs my_postgres_container`
- Verify database access: `docker exec -it my_postgres_container psql -U postgres`


### Check FastAPI Logs
```bash
docker logs my_fastapi_container
```


## Next Steps
- Deploy the application using Docker Compose in production
- Add authentication using JWT or OAuth2
- Integrate a frontend (React, Vue, etc.) to interact with the API


Follow these instructions to set up FastAPI with PostgreSQL and Docker successfully.