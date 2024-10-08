import os
from dotenv import load_dotenv
from fastapi import FastAPI


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}
