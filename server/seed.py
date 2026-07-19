from server.app import app

with app.app_context():
    print("Seed file ready.")