# routes.py
from flask import Blueprint, request, jsonify
from app import db, bcrypt
from models import User, Banner, Skill, Experience, Portfolio, Service, BlogPost, ContactMessage
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)
admin_bp = Blueprint('admin', __name__)
public_bp = Blueprint('public', __name__)


# routes.py continued...

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
  
    user = User.query.filter_by(username=username).first()
  
    if user and user.check_password(password):
        access_token = create_access_token(identity={'username': user.username})
        return jsonify({'token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


# routes.py continued...

@admin_bp.route('/admin/banner', methods=['PUT'])
@jwt_required()
def update_banner():
    data = request.get_json()
    banner = Banner.query.first()
    if not banner:
        banner = Banner()
        db.session.add(banner)

    banner.image_url = data.get('image_url')
    banner.cv_url = data.get('cv_url')
    db.session.commit()
    return jsonify({'message': 'Banner updated successfully'}), 200

# Similar routes for Skills, Experience, Portfolio, Services, Blog Posts

@admin_bp.route('/admin/skills', methods=['POST'])
@jwt_required()
def add_skill():
    data = request.get_json()
    new_skill = Skill(name=data.get('name'))
    db.session.add(new_skill)
    db.session.commit()
    return jsonify({'message': 'Skill added successfully'}), 201

@admin_bp.route('/admin/skills/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_skill(id):
    skill = Skill.query.get(id)
    if skill:
        db.session.delete(skill)
        db.session.commit()
        return jsonify({'message': 'Skill deleted successfully'}), 200
    else:
        return jsonify({'message': 'Skill not found'}), 404

# routes.py continued...

@public_bp.route('/banner', methods=['GET'])
def get_banner():
    banner = Banner.query.first()
    if banner:
        return jsonify({'image_url': banner.image_url, 'cv_url': banner.cv_url}), 200
    else:
        return jsonify({'message': 'Banner not found'}), 404

@public_bp.route('/skills', methods=['GET'])
def get_skills():
    skills = Skill.query.all()
    skills_list = [{'id': skill.id, 'name': skill.name} for skill in skills]
    return jsonify(skills_list), 200

# Similar routes for Experience, Portfolio, Services, Blog Posts

@public_bp.route('/contact', methods=['POST'])
def send_message():
    data = request.get_json()
    new_message = ContactMessage(
        name=data.get('name'),
        email=data.get('email'),
        message=data.get('message')
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'Message sent successfully'}), 201

@public_bp.route('/experience', methods=['GET'])
def get_experience():
    experiences = Experience.query.all()
    return jsonify([{'id': exp.id, 'title': exp.title, 'description': exp.description} for exp in experiences]), 200

@public_bp.route('/portfolio', methods=['GET'])
def get_portfolio():
    projects = Portfolio.query.all()
    return jsonify([{'id': proj.id, 'project_name': proj.project_name, 'description': proj.description} for proj in projects]), 200

@public_bp.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([{'id': srv.id, 'title': srv.title, 'description': srv.description} for srv in services]), 200

@public_bp.route('/blog', methods=['GET'])
def get_blog_posts():
    blog_posts = BlogPost.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in blog_posts]), 200


