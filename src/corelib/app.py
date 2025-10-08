
import sentry_sdk
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from corelib.api.router import make_health_check_router
from .utils import custom_generate_unique_id

def create_app(settings, api_router):

    if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
        sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        generate_unique_id_function=custom_generate_unique_id,
    )

    # Set all CORS enabled origins
    if settings.all_cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.all_cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    health_check_router = make_health_check_router()

    api_router.include_router(health_check_router, prefix="/utils")
    app.include_router(api_router, prefix=settings.API_V1_STR)
    return app