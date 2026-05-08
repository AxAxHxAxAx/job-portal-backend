from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    company = Column(String)
    location = Column(String)
    recruiter_id = Column(Integer, ForeignKey("users.id"))

class SavedJob(Base):
    __tablename__ = "savedjobs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    