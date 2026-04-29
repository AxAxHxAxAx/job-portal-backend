from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "UNIFIED"
ALGORITHM = "HS256"

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHM])
        email = payload.get("sub")
        name = payload.get("name")
        role = payload.get("role")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        return {
            "name": name, 
            "email": email, 
            "role": role
            }
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    