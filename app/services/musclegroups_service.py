from sqlalchemy.orm import Session
from data import models
from data import schemas

def create_muscle_group(db: Session, muscle_group: schemas.MuscleGroup):
    muscle_group = models.MuscleGroup(name=muscle_group.name)
    db.add(muscle_group)
    db.commit()
    db.refresh(muscle_group)
    return

def get_muscle_groups(db: Session):
    return db.query(models.MuscleGroup).all()

def get_muscle_group_by_name(db: Session, name: str):
    return db.query(models.MuscleGroup).filter(models.MuscleGroup.name == name).first()