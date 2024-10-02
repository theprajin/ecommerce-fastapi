from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.auth.router import router as auth_router
from src.common.exceptions import http_exception_handler
from fastapi.staticfiles import StaticFiles
from src.common.config import settings
from src.common.database import create_tables

# Call create_tables to ensure all tables are created before starting the app
create_tables()

# Initialize the FastAPI app
app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)

# Setup CORS (Cross-Origin Resource Sharing) middleware
# Allow origins can be restricted for security in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handler for HTTP exceptions (custom or otherwise)
app.add_exception_handler(HTTPException, http_exception_handler)


# Include routers from the different modules
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


# Root path for health check or basic info
@app.get("/")
def root():
    return {"message": "Welcome to the Full-Scale E-commerce Platform API"}


# Optional: you can add more global routes or configurations here
