# create_admin.py

from app import create_app, db
from models import User

def create_admin():
    app = create_app()
    with app.app_context():
        # Check if admin user already exists
        existing_user = User.query.filter_by(username='admin').first()
        if existing_user:
            print('Admin user already exists.')
            return

        # Create a new admin user
        username = 'user-dummy'  # You can change this
        password = 'pass-dummy'  # Use a strong password

        admin_user = User(username=username)
        admin_user.set_password(password)
        db.session.add(admin_user)
        db.session.commit()
        print('Admin user created successfully.')

if __name__ == '__main__':
    create_admin()
