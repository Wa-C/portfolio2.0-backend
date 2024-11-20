# add_banner_data.py

from app import create_app, db
from models import Banner

def add_banner_data():
    app = create_app()
    with app.app_context():
        # Check if a banner already exists
        existing_banner = Banner.query.first()
        if existing_banner:
            print("Banner data already exists.")
            return

        # Add new banner data
        banner = Banner(
            image_url='##################',  # Replace with actual URL
            cv_url='############'  # Replace with actual URL
        )
        db.session.add(banner)
        db.session.commit()
        print("Banner data added successfully.")

if __name__ == '__main__':
    add_banner_data()
