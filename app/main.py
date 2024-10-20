from fastapi import FastAPI
from data import database
from routers import user
from routers import workout
from routers import musclegroup

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

app.include_router(user.users_router)
app.include_router(workout.workouts_router)
app.include_router(musclegroup.musclegroup_router)
