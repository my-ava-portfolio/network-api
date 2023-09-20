import uvicorn
from litestar import Litestar, Router
from litestar.config.cors import CORSConfig
from litestar.openapi import OpenAPIConfig

from network_api.config import settings
from network_api.routers import network_api_routes


def set_app() -> Litestar:
    open_api_enabled = settings.OPENAPI_STATUS == "enabled"

    portfolio_base_route = Router(path=settings.API_PREFIX, route_handlers=network_api_routes)

    application = Litestar(
        openapi_config=OpenAPIConfig(
            title=settings.PROJECT_NAME, version=settings.PROJECT_NAME
        ) if open_api_enabled else None,
        route_handlers=[portfolio_base_route],
        cors_config=CORSConfig(allow_origins=settings.ORIGINS),
        dependencies={})

    return application


app = set_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1111)
