from functools import wraps
from flask import flash, render_template
from flask_login import current_user

def role_required(roles):
    """Decorator to require specific roles for access to a route"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('You must be logged in to access this page.', 'error')
                return render_template('access_denied.html')

            if current_user.role not in roles:
                flash('You do not have permission to access this function.', 'error')
                return render_template('access_denied.html')

            return func(*args, **kwargs)
        return wrapper
    return decorator

