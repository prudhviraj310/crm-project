from fastapi import FastAPI
from app.routes import user_routes  # ✅ Importing user routes

app = FastAPI()

# Default base route
@app.get("/")
def root():
    return {"message": "CRM Backend running"}

# ✅ Include all user-related routes under this prefix
app.include_router(
    user_routes.router,
    prefix="/api/users",  # So routes will be like /api/users/register, /api/users/login
    tags=["Users"]
)
