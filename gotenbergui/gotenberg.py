import os, json, requests, uvicorn, uuid
import shutil, aiofiles, sqlite3, base64
from os import environ, path
from loguru import logger
from fastapi import FastAPI, Request, File, Form, UploadFile
from fastapi.responses import UJSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder


app = FastAPI(title="Docker Composer", description="Generate docker-compose for tunning containers", version="1.0.0")
logger.info("Configuring app")
app = FastAPI(title="Deepstack Trainer", description="Train your deepstack AI server", version="1.0.0")
app.mount("/dist", StaticFiles(directory="dist"), name="dist")
app.mount("/js", StaticFiles(directory="dist/js"), name="js")
app.mount("/css", StaticFiles(directory="dist/css"), name="css")
app.mount("/images", StaticFiles(directory="dist/images"), name="images")
templates = Jinja2Templates(directory="templates/")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home(request: Request):
    logger.info("loading default page")
    server_url = "http://192.168.0.252:3010"
    return templates.TemplateResponse('index.html', context={'request': request, 'server_url' : server_url})

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3011)