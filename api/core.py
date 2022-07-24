# -*- coding: utf-8 *-*

from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from dotenv import load_dotenv
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.config.docs import *
from api.config.cors import *
from api.config.api import API_NAME, API_VERSION, API_DESCRIPTION, API_PREFIX
from api.routes.api import router


api = FastAPI(
    docs_url=None,
    redoc_url=None,
    title=API_NAME,
    description=API_DESCRIPTION,
    version=API_VERSION,
    openapi_tags=METADATA,
    terms_of_service=TERMS,
    contact=CONTACT,
    license_info=LICENSE
)


api.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=CREDENTIALS,
    allow_methods=METHODS,
    allow_headers=HEADERS,
)


api.mount('/public', StaticFiles(directory='public'), name='public')


@api.on_event('startup')
async def startup_event():
    pass


@api.on_event('shutdown')
def shutdown_event():
    pass


api.include_router(router)


@api.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url='/openapi.json',
        title=API_NAME,
        swagger_favicon_url='/public/assets/img/favicon.png'
    )


@api.get('/', tags=['Root'])
def root():
    return RedirectResponse(url=API_PREFIX, status_code=303)


@api.get(API_PREFIX, include_in_schema=False, tags=['Root'])
def actual_version():
    return {'Hello': 'World'}


load_dotenv()