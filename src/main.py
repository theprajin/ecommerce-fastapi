from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from src.auth.router import router as auth_router
from src.common.exceptions import http_exception_handler
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
    return {
        "message": "Welcome to the Full-Scale E-commerce Platform API",
        "version": "1.0.0",
        "documentation": "https://ecommerce-fastapi-i6u5.onrender.com/docs",
        "documentation2": "https://ecommerce-fastapi-i6u5.onrender.com/redoc",
        "documentation2": "https://ecommerce-fastapi-i6u5.onrender.com/rapidoc",
    }


@app.get("/rapidoc", include_in_schema=False)
async def custom_docs():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>RapiDoc</title>
        <script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script>
    </head>
    <body>
        <rapi-doc 
            spec-url="/openapi.json" 
            render-style="read" 
            theme="light"
            show-header="true"
            allow-spec-url-load="false"
            allow-search="true"
            show-method-in-nav-bar="true"
        ></rapi-doc>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# Optional: you can add more global routes or configurations here
