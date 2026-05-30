from app import create_app, db
from init_db import seed_database

app = create_app()

# Initialize database tables and seed original records before starting the server
with app.app_context():
    db.create_all()
    seed_database()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)