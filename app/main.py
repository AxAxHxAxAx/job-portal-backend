from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User
from app.routes import user as user_routes

app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.get("/")
def read_root():
    return {"message": "Job Portal API Running 🚀"}

app.include_router(user_routes.router)