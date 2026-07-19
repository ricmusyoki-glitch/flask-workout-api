from marshmallow import Schema, fields, validate


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=2)
    )

    category = fields.Str(
        required=True,
        validate=validate.Length(min=2)
    )

    equipment_needed = fields.Bool(required=True)


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    workout_id = fields.Int(required=True)

    exercise_id = fields.Int(required=True)

    sets = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    reps = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    duration_seconds = fields.Int()


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)

    date = fields.Date(required=True)

    duration_minutes = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    notes = fields.Str()

    exercises = fields.Nested(
        ExerciseSchema,
        many=True,
        dump_only=True
    )

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)