from flask import Flask
from app.config import Config
from app.models import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.transactions import transactions_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(transactions_bp)
    
    # Global context processor to make helper functions available in templates
    @app.context_processor
    def inject_helpers():
        def format_currency(value):
            return f"₹{value:,.2f}"
        return dict(format_currency=format_currency)
        
    return app
