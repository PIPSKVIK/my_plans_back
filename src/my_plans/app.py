from fastapi import FastAPI

from .api import router

app = FastAPI(
    title='My Plans'
)
app.include_router(router)
