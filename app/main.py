from fastapi import FastAPI
from routers import user
from routers import workout

app = FastAPI()

app.include_router(user.users_router)
app.include_router(workout.workouts_router)
