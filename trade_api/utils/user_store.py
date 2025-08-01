from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
users_db = {}  # username -> {hashed_password}

def create_user(username: str, password: str):
    if username in users_db:
        raise ValueError("User already exists.")
    users_db[username] = {
        "username": username,
        "hashed_password": pwd_context.hash(password)
    }

def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    if not user:
        return False
    if not pwd_context.verify(password, user["hashed_password"]):
        return False
    return user
