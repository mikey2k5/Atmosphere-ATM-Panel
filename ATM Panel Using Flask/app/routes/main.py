from flask import Blueprint, render_template, session, redirect, url_for
from app.services.bank_service import BankService
from app.utils.decorators import login_required

main_bp = Blueprint('main', __name__)

@main_bp.route("/dashboard")
@login_required
def dashboard():
    acc_num = session["account"]
    account = BankService.get_account(acc_num)
    if not account:
        session.clear()
        return redirect(url_for("auth.login"))
        
    analytics = BankService.get_analytics(acc_num)
    recent_tx = BankService.get_transaction_history(acc_num, limit=5)
    
    return render_template(
        "dashboard.html",
        name=account.account_holder_name,
        account_number=account.account_number,
        balance=account.balance,
        status=account.account_status,
        analytics=analytics,
        transactions=recent_tx
    )

@main_bp.route("/balance")
@login_required
def balance():
    acc_num = session["account"]
    account = BankService.get_account(acc_num)
    if not account:
        session.clear()
        return redirect(url_for("auth.login"))
        
    recent_tx = BankService.get_transaction_history(acc_num, limit=10)
    
    return render_template(
        "balance.html",
        balance=account.balance,
        account_number=account.account_number,
        name=account.account_holder_name,
        transactions=recent_tx
    )
