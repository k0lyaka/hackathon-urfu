from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from urfu.application.errors import AppError


async def error_handler(request: Request, exc: Exception) -> JSONResponse:
    if isinstance(exc, AppError):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.message,
            },
        )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
        },
    )


def setup_error_handler(app: FastAPI) -> None:
    app.add_exception_handler(Exception, error_handler)
