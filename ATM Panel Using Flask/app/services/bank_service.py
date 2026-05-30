from app.models import db, Account, Transaction
from werkzeug.security import check_password_hash, generate_password_hash

class BankError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class BankService:
    @staticmethod
    def get_account(account_number):
        return Account.query.filter_by(account_number=account_number).first()

    @staticmethod
    def authenticate_account(account_number, pin):
        account = BankService.get_account(account_number)
        if not account:
            raise BankError("Account does not exist")
        if account.account_status != "Active":
            raise BankError("Account is blocked")
        if not check_password_hash(account.pin_hash, str(pin)):
            raise BankError("Invalid PIN")
        return account

    @staticmethod
    def deposit(account_number, amount):
        account = BankService.get_account(account_number)
        if not account:
            raise BankError("Account not found")
        if account.account_status != "Active":
            raise BankError("Account is blocked")
        
        if amount <= 500:
            raise BankError("Deposit amount must be greater than ₹500")
        if amount % 100 != 0:
            raise BankError("Deposit amount must be in multiples of ₹100")
            
        account.balance += amount
        
        transaction = Transaction(
            account_number=account_number,
            type="Deposit",
            amount=float(amount),
            description=f"Cash Deposit of ₹{amount}"
        )
        db.session.add(transaction)
        db.session.commit()
        return account.balance

    @staticmethod
    def withdraw(account_number, amount):
        account = BankService.get_account(account_number)
        if not account:
            raise BankError("Account not found")
        if account.account_status != "Active":
            raise BankError("Account is blocked")
        
        if amount <= 500:
            raise BankError("Amount must be greater than ₹500")
        if amount % 100 != 0:
            raise BankError("Amount must be in multiples of ₹100")
        if amount >= 20000:
            raise BankError("Per withdrawal limit is ₹20,000")
        if amount > account.balance:
            raise BankError("Insufficient balance")
            
        account.balance -= amount
        
        transaction = Transaction(
            account_number=account_number,
            type="Withdrawal",
            amount=float(amount),
            description=f"Cash Withdrawal of ₹{amount}"
        )
        db.session.add(transaction)
        db.session.commit()
        return account.balance

    @staticmethod
    def change_pin(account_number, old_pin, new_pin):
        account = BankService.get_account(account_number)
        if not account:
            raise BankError("Account not found")
        
        if not check_password_hash(account.pin_hash, str(old_pin)):
            raise BankError("Old PIN is incorrect")
        if not str(new_pin).isdigit() or len(str(new_pin)) != 4:
            raise BankError("New PIN must be 4 digits")
            
        account.pin_hash = generate_password_hash(str(new_pin))
        
        transaction = Transaction(
            account_number=account_number,
            type="PIN Change",
            amount=0.0,
            description="Secure PIN Modification"
        )
        db.session.add(transaction)
        db.session.commit()
        return True

    @staticmethod
    def get_transaction_history(account_number, limit=10):
        return Transaction.query.filter_by(account_number=account_number)\
            .order_by(Transaction.timestamp.desc())\
            .limit(limit).all()

    @staticmethod
    def get_analytics(account_number):
        account = BankService.get_account(account_number)
        if not account:
            return None
        
        transactions = Transaction.query.filter_by(account_number=account_number).all()
        total_deposited = sum(t.amount for t in transactions if t.type == "Deposit")
        total_withdrawn = sum(t.amount for t in transactions if t.type == "Withdrawal")
        transaction_count = len(transactions)
        
        return {
            "balance": account.balance,
            "total_deposited": total_deposited,
            "total_withdrawn": total_withdrawn,
            "transaction_count": transaction_count
        }
