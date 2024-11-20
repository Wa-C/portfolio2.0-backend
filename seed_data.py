# seed_data.py

from app import create_app, db
from models import Skill, Experience, Portfolio, Service, BlogPost

def seed_data():
    app = create_app()
    with app.app_context():
        # Seed Skills
        skills = [
            Skill(name='Python'),
            Skill(name='JavaScript'),
            Skill(name='React'),
            # Add more skills as needed
        ]
        db.session.bulk_save_objects(skills)

        # Seed Experiences
        experiences = [
            Experience(title='Software Engineer at XYZ Corp', description='Developed web applications using React and Node.js'),
            # Add more experiences
        ]
        db.session.bulk_save_objects(experiences)

        # Seed Portfolio Projects
        projects = [
            Portfolio(project_name='Project Alpha', description='An AI-powered platform', image_url='http://example.com/image.png', project_url='http://example.com'),
            # Add more projects
        ]
        db.session.bulk_save_objects(projects)

        # Seed Services
        services = [
            Service(title='Web Development', description='Building responsive websites'),
            # Add more services
        ]
        db.session.bulk_save_objects(services)

        # Seed Blog Posts
        blog_posts = [
            BlogPost(title='Understanding Machine Learning', content='An introduction to ML concepts'),
            # Add more blog posts
        ]
        db.session.bulk_save_objects(blog_posts)

        db.session.commit()
        print('Data seeded successfully.')

if __name__ == '__main__':
    seed_data()
