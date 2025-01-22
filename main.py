
from uvicorn import run
from configs.app_config import envs
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
)
from routers.items_router import items_router
from configs.database import create_db_and_tables

create_db_and_tables()

app = FastAPI(
    title=envs.TITLE_APP, version='v0.1',
    description=envs.DESCRIPTION_APP,
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
)

# region SwaggerControllers
app.mount('/static', StaticFiles(directory='static'), name='static')
@app.get("/docs", include_in_schema=False)
def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )

@app.get("/redoc", include_in_schema=False)
def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )
# endregion

app.include_router(router=items_router)

@app.get("/Hello_Wolrd", name='Hello_World')
def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    run('main:app', host=envs.HOST, port=envs.PORT, reload=True)
    



