from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = 'accounts'
    
    account_number = db.Column(db.String(20), primary_key=True)
    account_holder_name = db.Column(db.String(100), nullable=False)
    pin_hash = db.Column(db.String(256), nullable=False)
    account_status = db.Column(db.String(20), default='Active', nullable=False)  # 'Active' or 'Blocked'
    balance = db.Column(db.Float, default=0.0, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    
    transactions = db.relationship('Transaction', backref='account', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "account_holder_name": self.account_holder_name,
            "account_status": self.account_status,
            "balance": self.balance,
            "created_at": self.created_at.isoformat()
        }

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_number = db.Column(db.String(20), db.ForeignKey('accounts.account_number'), nullable=False)
    type = db.Column(db.String(20), nullable=False)  # 'Deposit', 'Withdrawal', 'PIN Change'
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "account_number": self.account_number,
            "type": self.type,
            "amount": self.amount,
            "description": self.description,
            "timestamp": self.timestamp.isoformat()
        }
