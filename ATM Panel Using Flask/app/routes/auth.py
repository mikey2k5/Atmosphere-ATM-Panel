from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.services.bank_service import BankService, BankError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/", methods=["GET", "POST"])
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if "account" in session:
        return redirect(url_for("main.dashboard"))
        
    error = None
    if request.method == "POST":
        acc = request.form.get("account", "").strip()
        pin = request.form.get("pin", "").strip()
        
        if not acc or not pin:
            error = "Account and PIN are required"
        else:
            try:
                account = BankService.authenticate_account(acc, pin)
                session["account"] = account.account_number
                return redirect(url_for("main.dashboard"))
            except BankError as e:
                error = e.message
                
    return render_template("login.html", error=error)

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Successfully logged out.", "success")
    return redirect(url_for("auth.login"))
