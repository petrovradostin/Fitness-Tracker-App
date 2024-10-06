from sqlalchemy.orm import Session
from data import models
from data import schemas



def create_workout(db: Session, workout: schemas.WorkoutCreate, user_id: int):
    db_workout = models.Workout(**workout.model_dump(), user_id=user_id)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

def get_user_workouts(db: Session, user_id: int):
    return db.query(models.Workout).filter(models.Workout.user_id == user_id).all()
