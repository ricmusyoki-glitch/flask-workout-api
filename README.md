# Flask SQLAlchemy Workout Application Backend

## Project Description

This project is a RESTful backend API built with Flask, Flask-SQLAlchemy, Flask-Migrate, and Marshmallow.

The application allows personal trainers to manage workouts and exercises. Exercises can be reused across multiple workouts using a many-to-many relationship implemented through the WorkoutExercise association table.

---

## Technologies Used

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- SQLite
- Pipenv

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate into the project

```bash
cd flask-workout-api
```

Install dependencies

```bash
pipenv install
```

Activate the virtual environment

```bash
pipenv shell
```

---

## Database Setup

Initialize migrations

```bash
flask db init
```

Create a migration

```bash
flask db migrate -m "Initial migration"
```

Apply the migration

```bash
flask db upgrade
```

Seed the database

```bash
python -m server.seed
```

---

## Running the Application

```bash
export FLASK_APP=server.app
flask run
```

The server will start at

```
http://127.0.0.1:5000
```

---

## API Endpoints

### Exercises

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /exercises | Get all exercises |
| GET | /exercises/<id> | Get one exercise |
| POST | /exercises | Create an exercise |
| DELETE | /exercises/<id> | Delete an exercise |

---

### Workouts

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /workouts | Get all workouts |
| GET | /workouts/<id> | Get one workout |
| POST | /workouts | Create a workout |
| DELETE | /workouts/<id> | Delete a workout |

---

### Workout Exercises

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /workouts/<workout_id>/exercises | Add an exercise to a workout |

---

## Database Models

- Exercise
- Workout
- WorkoutExercise

---

## Features

- SQLAlchemy Models
- Model Relationships
- Marshmallow Serialization
- Schema Validation
- Model Validation
- Database Migrations
- Seed Data
- REST API

---

## Author

Ric Musyoki