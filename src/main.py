from fastapi import FastAPI
from src.adapters.api import router

app = FastAPI()
app.include_router(router)