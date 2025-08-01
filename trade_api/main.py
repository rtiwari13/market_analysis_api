from fastapi import FastAPI
from api.endpoints import router as api_router
from api.auth_routes import router as auth_router
from slowapi.middleware import SlowAPIMiddleware
from auth.dependencies import rate_limiter

app = FastAPI(title="Market Analysis API")
app.state.limiter = rate_limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(auth_router)
app.include_router(api_router)
