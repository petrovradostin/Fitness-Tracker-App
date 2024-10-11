from sqlalchemy.orm import Session
from data import models
from data import schemas

def create_exercise(db: Session, exercise: schemas.ExerciseCreate):
    exercise = models.Exercise(name=exercise.name, muscle_group_id=exercise.muscle_group_id)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise

def get_exercises(db: Session, muscle_group_id: int):
    return db.query(models.Exercise).filter(models.Exercise.muscle_group_id == muscle_group_id).all()
