import uvicorn
from starlite import Starlite, CORSConfig, Provide, OpenAPIConfig, Router

from starlite.openapi.controller import OpenAPISchemaResponse
from starlite.enums import OpenAPIMediaType

from network_api.config import settings
from network_api.routers import network_api_routes


def build_openapi_yml() -> None:
    if settings.OPENAPI_STATUS == "enabled":
        with open("openapi.yaml", "wb+") as output:
            api_doc_schema = OpenAPISchemaResponse(content=app.openapi_schema, media_type=OpenAPIMediaType.OPENAPI_YAML)
            output.write(api_doc_schema.body)


def set_app() -> Starlite:
    open_api_enabled = settings.OPENAPI_STATUS == "enabled"

    portfolio_base_route = Router(path=settings.API_PREFIX, route_handlers=network_api_routes)

    application = Starlite(
        openapi_config=OpenAPIConfig(
            title=settings.PROJECT_NAME, version=settings.PROJECT_NAME
        ) if open_api_enabled else None,
        route_handlers=[portfolio_base_route],
        cors_config=CORSConfig(allow_origins=settings.ORIGINS),
        dependencies={})

    return application


app = set_app()

if __name__ == "__main__":
    build_openapi_yml()
    uvicorn.run(app, host="0.0.0.0", port=1111)
