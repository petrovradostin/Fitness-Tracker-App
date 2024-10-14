from sqlalchemy.orm import Session
from data import models
from data import schemas

def create_set(db: Session, set: schemas.SetCreate):
    set = models.Sets(set_number=set.set_number, exercise_id=set.exercise_id)
    db.add(set)
    db.commit()
    db.refresh(set)
    return set

def get_set_by_exercise(db: Session, exercise_id: int):
    return db.query(models.Set).filter(models.Set.exercise_id == exercise_id).all()
