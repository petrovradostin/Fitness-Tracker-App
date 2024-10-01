from sqlalchemy.orm import Session
from data.models import Workout
from data.schemas import WorkoutCreate



def create_workout(db: Session, workout: WorkoutCreate, user_id: int):
    db_workout = Workout(**workout.model_dump(), owner_id=user_id)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

def get_user_workouts(db: Session, user_id: int):
    return db.query(Workout).filter(Workout.owner_id == user_id).all()
