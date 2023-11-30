"""FastAPI application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse
from app.core.settings import settings
from app.routes import (test)


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """

    app = FastAPI(
        title=settings.fastapi_title,
        description=settings.fastapi_desc,
        version=settings.fastapi_version,
        default_response_class=UJSONResponse,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # Main router for the API.
    app.include_router(test.router)
    return app
