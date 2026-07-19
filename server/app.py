from flask import Flask, request, jsonify
from datetime import datetime

from server.config import db, migrate
from server.models import Exercise, Workout, WorkoutExercise
from server.schemas import (
    exercise_schema,
    exercises_schema,
    workout_schema,
    workouts_schema,
    workout_exercise_schema,
)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workout.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)


@app.route("/")
def index():
    return {"message": "Workout API running"}




@app.get("/exercises")
def get_exercises():
    exercises = Exercise.query.all()
    return exercises_schema.dump(exercises), 200


@app.get("/exercises/<int:id>")
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    return exercise_schema.dump(exercise), 200


@app.post("/exercises")
def create_exercise():
    data = request.get_json()

    errors = exercise_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    exercise = Exercise(
        name=data["name"],
        category=data["category"],
        equipment_needed=data["equipment_needed"]
    )

    db.session.add(exercise)
    db.session.commit()

    return exercise_schema.dump(exercise), 201


@app.delete("/exercises/<int:id>")
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({"message": "Exercise deleted"}), 200



@app.get("/workouts")
def get_workouts():
    workouts = Workout.query.all()
    return workouts_schema.dump(workouts), 200


@app.get("/workouts/<int:id>")
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return workout_schema.dump(workout), 200


@app.post("/workouts")
def create_workout():
    data = request.get_json()

    errors = workout_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    workout = Workout(
        date=datetime.strptime(
            data["date"],
            "%Y-%m-%d"
        ).date(),
        duration_minutes=data["duration_minutes"],
        notes=data.get("notes")
    )

    db.session.add(workout)
    db.session.commit()

    return workout_schema.dump(workout), 201


@app.delete("/workouts/<int:id>")
def delete_workout(id):
    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return jsonify({"message": "Workout deleted"}), 200



@app.post("/workouts/<int:workout_id>/exercises")
def add_exercise_to_workout(workout_id):

    workout = Workout.query.get_or_404(workout_id)

    data = request.get_json()

    errors = workout_exercise_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    Exercise.query.get_or_404(data["exercise_id"])

    workout_exercise = WorkoutExercise(
        workout_id=workout.id,
        exercise_id=data["exercise_id"],
        sets=data["sets"],
        reps=data["reps"],
        duration_seconds=data.get("duration_seconds")
    )

    db.session.add(workout_exercise)
    db.session.commit()

    return workout_exercise_schema.dump(workout_exercise), 201


if __name__ == "__main__":
    app.run(debug=True)