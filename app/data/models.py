from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# Association table for the many-to-many relationship between Workout and MuscleGroup
workout_muscle_group = Table(
    'workout_muscle_group', Base.metadata,
    Column('workout_id', Integer, ForeignKey('workouts.id'), primary_key=True),
    Column('muscle_group_id', Integer, ForeignKey('musclegroup.id'), primary_key=True)
)

# User Table: A user can have many workouts
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # One-to-many relationship with Workout
    workouts = relationship("Workout", back_populates="user")


# Workout Table: A workout belongs to a user and targets multiple muscle groups
class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    date_posted = Column(DateTime, default=datetime.now)

    # Foreign key to reference the user that created the workout
    user_id = Column(Integer, ForeignKey('user.id'))

    # Relationship with MuscleGroup using the association table
    muscle_groups = relationship("MuscleGroup", secondary=workout_muscle_group, back_populates="workouts")

    # Relationship back to User
    user = relationship("User", back_populates="workouts")


# MuscleGroup Table: Each muscle group can be part of many workouts and have multiple exercises
class MuscleGroup(Base):
    __tablename__ = "musclegroup"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    # Many-to-many relationship with Workout
    workouts = relationship("Workout", secondary=workout_muscle_group, back_populates="muscle_groups")

    # One-to-many relationship with Exercise
    exercises = relationship("Exercise", back_populates="muscle_group")


# Exercise Table: An exercise targets one muscle group, and it can be part of many set
class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    # Foreign key to reference the muscle group that the exercise targets
    muscle_group_id = Column(Integer, ForeignKey('musclegroup.id'))

    # Relationship back to MuscleGroup
    muscle_group = relationship("MuscleGroup", back_populates="exercises")

    # One-to-many relationship with Set
    set = relationship("Set", back_populates="exercise")


# Set Table: A set contains multiple reps for an exercise
class Set(Base):
    __tablename__ = "set"
    
    id = Column(Integer, primary_key=True, index=True)
    set_number = Column(Integer, index=True)

    # Foreign key to reference the Exercise it belongs to
    exercise_id = Column(Integer, ForeignKey('exercise.id'))
    
    # Relationship back to Exercise
    exercise = relationship("Exercise", back_populates="set")

    # One-to-many relationship with Reps
    reps = relationship("Reps", back_populates="set")


# Reps Table: Each set contains multiple reps with weight
class Reps(Base):
    __tablename__ = "reps"

    id = Column(Integer, primary_key=True, index=True)
    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)

    # Foreign key to reference the Set it belongs to
    set_id = Column(Integer, ForeignKey('set.id'))

    # Relationship back to Set
    set = relationship("Set", back_populates="reps")
