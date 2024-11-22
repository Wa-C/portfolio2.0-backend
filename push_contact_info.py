from app import create_app, db
from models import ContactMessage

def add_contact_message():
    app = create_app()
    with app.app_context():
        # Check if a contact message already exists
        existing_message = ContactMessage.query.first()
        if existing_message:
            print("A contact message already exists in the database.")
            print(f"Name: {existing_message.name}")
            print(f"Email: {existing_message.email}")
            print(f"Message: {existing_message.message}")
            print(f"Date Sent: {existing_message.date_sent}")
            return

        # Input contact message details
        name = "Syed Wassi Ul Haque "
        email = "syedwassiulhaque@gmail.com "
        message = "Always Available "

        # Add new contact message
        contact_message = ContactMessage(
            name=name,
            email=email,
            message=message
        )
        db.session.add(contact_message)
        db.session.commit()
        print("Contact message added successfully.")

if __name__ == '__main__':
    add_contact_message()
