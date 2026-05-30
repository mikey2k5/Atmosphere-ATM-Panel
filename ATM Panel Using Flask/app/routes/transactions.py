from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from app.services.bank_service import BankService, BankError
from app.utils.decorators import login_required

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route("/withdraw", methods=["GET", "POST"])
@login_required
def withdraw():
    acc_num = session["account"]
    account = BankService.get_account(acc_num)
    if not account:
        session.clear()
        return redirect(url_for("auth.login"))
        
    error = None
    success = None
    
    if request.method == "POST":
        try:
            amount_str = request.form.get("amount", "")
            if not amount_str:
                error = "Amount is required"
            else:
                try:
                    amount = int(amount_str)
                except ValueError:
                    error = "Amount must be a valid number"
                    return render_template("withdraw.html", error=error, balance=account.balance)
                
                new_balance = BankService.withdraw(acc_num, amount)
                success = f"Withdrawal successful! ₹{amount:,.2f} withdrawn from your account."
                account = BankService.get_account(acc_num)  # Refresh balance
        except BankError as e:
            error = e.message
            
    return render_template("withdraw.html", error=error, success=success, balance=account.balance)

@transactions_bp.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    acc_num = session["account"]
    account = BankService.get_account(acc_num)
    if not account:
        session.clear()
        return redirect(url_for("auth.login"))
        
    error = None
    success = None
    
    if request.method == "POST":
        try:
            amount_str = request.form.get("amount", "")
            if not amount_str:
                error = "Amount is required"
            else:
                try:
                    amount = int(amount_str)
                except ValueError:
                    error = "Amount must be a valid number"
                    return render_template("deposit.html", error=error, balance=account.balance)
                    
                new_balance = BankService.deposit(acc_num, amount)
                success = f"Deposit successful! ₹{amount:,.2f} added to your account."
                account = BankService.get_account(acc_num)  # Refresh balance
        except BankError as e:
            error = e.message
            
    return render_template("deposit.html", error=error, success=success, balance=account.balance)

@transactions_bp.route("/changepin", methods=["GET", "POST"])
@login_required
def changepin():
    acc_num = session["account"]
    error = None
    success = None
    
    if request.method == "POST":
        old_pin = request.form.get("old_pin", "").strip()
        new_pin = request.form.get("new_pin", "").strip()
        
        if not old_pin or not new_pin:
            error = "Both old and new PIN are required"
        else:
            try:
                BankService.change_pin(acc_num, old_pin, new_pin)
                success = "PIN changed successfully! Your account is now secured with your new credentials."
            except BankError as e:
                error = e.message
                
    return render_template("changepin.html", error=error, success=success)
