from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from slowapi import Limiter
from .jwt_handler import verify_jwt_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
rate_limiter = Limiter(key_func=lambda request: request.client.host)

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_jwt_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return user
