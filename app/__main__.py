import uvicorn
from app.core.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "app.routes.application:get_app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        # TODO: if only show open api docs if env is in these from three
        # SHOW_DOCS_ENVIRONMENT = (
        # "local",
        # "staging",
        # "dev",
        # )  # explicit list of allowed envs
        reload=settings.uvicorn_reload,
        log_level=settings.log_level.value.lower(),
        factory=True,
        timeout_keep_alive=settings.timeout_keep_alive,
    )


if __name__ == "__main__":
    main()
