from app.models import db, Account, Transaction
from werkzeug.security import generate_password_hash

def seed_database():
    # Check if Account table has data
    if Account.query.first() is not None:
        print("Database already seeded.")
        return
        
    print("Seeding database with original ATM accounts...")
    
    # Original student accounts data from accounts.py:
    accounts_to_seed = [
        {
            "account_number": "12316600",
            "account_holder_name": "Syed Khadar Ali",
            "pin": "1123",
            "account_status": "Active",
            "balance": 69000.0
        },
        {
            "account_number": "12316601",
            "account_holder_name": "Syed Moulali",
            "pin": "7789",
            "account_status": "Active",
            "balance": 10000.0
        },
        {
            "account_number": "12316602",
            "account_holder_name": "Syed Rahamathunnisa",
            "pin": "1231",
            "account_status": "Blocked",
            "balance": 67.0
        }
    ]
    
    for data in accounts_to_seed:
        acc = Account(
            account_number=data["account_number"],
            account_holder_name=data["account_holder_name"],
            pin_hash=generate_password_hash(data["pin"]),
            account_status=data["account_status"],
            balance=data["balance"]
        )
        db.session.add(acc)
        
        # Add a record for initial balance seed
        tx = Transaction(
            account_number=data["account_number"],
            type="Deposit",
            amount=data["balance"],
            description="System Initialization - Balance Seed"
        )
        db.session.add(tx)
        
    db.session.commit()
    print("Database seeding completed successfully.")

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    with app.app_context():
        db.create_all()
        seed_database()
