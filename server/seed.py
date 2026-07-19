from datetime import date

from server.app import app
from server.config import db
from server.models import Exercise, Workout, WorkoutExercise


with app.app_context():

    print("Clearing database...")

    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Creating exercises...")

    squat = Exercise(
        name="Squat",
        category="Strength",
        equipment_needed=False
    )

    bench = Exercise(
        name="Bench Press",
        category="Strength",
        equipment_needed=True
    )

    running = Exercise(
        name="Running",
        category="Cardio",
        equipment_needed=False
    )

    db.session.add_all([squat, bench, running])
    db.session.commit()

    print("Creating workout...")

    workout = Workout(
        date=date.today(),
        duration_minutes=60,
        notes="Full body workout"
    )

    db.session.add(workout)
    db.session.commit()

    print("Adding workout exercises...")

    we1 = WorkoutExercise(
        workout_id=workout.id,
        exercise_id=squat.id,
        sets=4,
        reps=10,
        duration_seconds=0
    )

    we2 = WorkoutExercise(
        workout_id=workout.id,
        exercise_id=bench.id,
        sets=3,
        reps=8,
        duration_seconds=0
    )

    db.session.add_all([we1, we2])
    db.session.commit()

    print("Database seeded successfully!")