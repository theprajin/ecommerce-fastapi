from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class AppException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


class ItemNotFoundException(AppException):
    def __init__(self, item: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{item} not found"
        )


class InvalidCredentialsException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )


class TokenExpiredException(AppException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired"
        )


# Global exception handler for uncaught exceptions
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code, content=jsonable_encoder({"detail": exc.detail})
    )
