import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from uvicorn import run as app_run
from fastapi.responses import JSONResponse

def set_env_variable(env_file_path:str):
    pass


app = FastAPI()
origin = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/train")
async def train(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # Process the uploaded file as needed
        return JSONResponse(content={"message": "File received successfully"})
    except Exception as e:
        raise NetworkSecurityException(e, sys)