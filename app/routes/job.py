from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.job import Job
from app.schemas.job import JobCreate
from app.auth.role_checker import require_role
from app.models.application import Application
from app.models.user import User
from app.schemas.job import UpdateJob

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/jobs")
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(require_role("recruiter"))
):
    new_job = Job(
        title = job.title,
        description = job.description,
        company = job.company,
        location = job.location,
        recruiter_id = user["id"]
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {"message": "Job created successfully"}

@router.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    return jobs

@router.post("/apply/{job_id}")
def apply_job(
    job_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(require_role("user"))
):
    existing = db.query(Application).filter(
        Application.user_id == user["id"],
        Application.job_id == job_id
    ).first()


    if existing:
        return {"message": "Already applied"}

    application = Application(
        user_id = user["id"],
        job_id = job_id
    )

    db.add(application)
    db.commit()

    return {"message": "Applied successfully"}

@router.get("/my-applications")
def get_my_applicatons(
    db: Session = Depends(get_db),
    user: dict = Depends(require_role("user"))
):
    results = db.query(Job).join(Application).filter(Application.user_id == user["id"]).all()

    return results

@router.get("/job_applications")
def get_job_applications(
    db: Session = Depends(get_db),
    user: dict = Depends(require_role("recruiter"))
):
    results = db.query(
        User.name,
        User.email,
        Job.title
    ).join(
        Application, Application.user_id == User.id
    ).join(
        Job, Job.id == Application.job_id
    ).filter(
        Job.recruiter_id == user["id"]
    ).all()

    data = []

    for result in results:
        data.append({
            "name": result.name,
            "email": result.email,
            "job_title": result.title
        })

    return data

@router.put("/updatejob/{job_id}")
def update_job(
    job_id: int,
    updated_job: UpdateJob,
    db: Session = Depends(get_db),
    user: dict = Depends(require_role("recruiter"))
):
    job = db.query(Job).filter(
        Job.id == job_id,
        Job.recruiter_id == user["id"]
    ).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job.title = updated_job.title
    job.description = updated_job.description
    job.company = updated_job.company
    job.location = updated_job.location

    db.commit()
    db.refresh(job)

    return {"message": "Job updated successfully"}