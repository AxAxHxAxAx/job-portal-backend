from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    description: str
    company: str
    location: str

class UpdateJob(BaseModel):
    title: str
    description: str
    company: str
    location: str