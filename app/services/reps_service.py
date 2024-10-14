from sqlalchemy.orm import Session
from data import schemas
from data import models

def create_reps(db: Session, reps: schemas.RepsCreate):
    reps = models.Reps(reps=reps.reps, weight=reps.weight, set_id=reps.set_id)
    db.add(reps)
    db.commit()
    db.refresh(reps)
    return reps

def get_reps_by_set(db: Session, set_id: int):
    return db.query(models.Reps).filter(models.Reps.set_id == set_id).all()
