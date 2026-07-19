from flask import Flask
from server.config import db, migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workout.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)

from server import models

@app.route("/")
def index():
    return {
        "message": "Workout API running"
    }

if __name__ == "__main__":
    app.run(port=5555, debug=True)