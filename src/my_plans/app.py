from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router

origins = ["*"]

app = FastAPI(
    title='My Plans'
)
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
