from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from illumination.controllers import router as illumination_router

app = FastAPI()
app.include_router(illumination_router)


def custom_openapi() -> dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Illumination hexagonal architecture",
        version="1.0.0",
        description="Hexagonal architecture in Python",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
