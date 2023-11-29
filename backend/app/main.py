from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette import status

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "You have accessed a very very private machine - Taka"}
