import uvicorn
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Registration"],
)


@app.get("/users/me", description="user info")
def protected_route(user: User = Depends(fastapi_users.current_user())):
    return {"username": user.username, "salary": user.salary, "salary_increase_date": user.salary_increase_date}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
