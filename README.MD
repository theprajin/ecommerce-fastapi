# Ecommerce App in FastAPI

## Setup the project

- first create virtual environment using pip and activate the virtual env
- then install the necessary package using the command "pip install -r requirements.txt"
- the create the .env file
- Don't forget to create a postgres database via pgadmin

### In .env file

#### create variable as below:

- DATABASE_URL=postgresql://your_username:your_password@localhost/ecommerce_db
- JWT_SECRET_KEY=your_secret_key
- DEBUG=True
- PROJECT_NAME="E-commerce Platform"

## Start the server

- uvicorn src.main:app --reload


## Testing API endpoint

- http://localhost:5000/api/v1/docs
- http://localhost:5000/api/v1/redoc

## If you want to test API through deployed link click below:

- https://ecommerce-fastapi-i6u5.onrender.com/docs
- https://ecommerce-fastapi-i6u5.onrender.com/redoc