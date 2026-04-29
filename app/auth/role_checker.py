from fastapi import HTTPException, Depends
from app.auth.dependencies import get_current_user

def require_role(required_role: str):
    def role_checker(user: dict = Depends(get_current_user)):
        if user["role"] != required_role:
            raise HTTPException(status_code=403, detail= "Access Denied")
        return user
    return role_checker