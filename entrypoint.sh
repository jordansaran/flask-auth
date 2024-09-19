#!/bin/bash
flask db upgrade

# Check if users exist, if not, create them
python << END
from app import app, db
from api.src.models.user import User
from sqlalchemy.exc import IntegrityError

with app.app_context():
    user_exists = User.query.filter_by(username='user').first()
    if not user_exists:
        user = User(
            username='user',
            role='user',
            password='L0XuwPOdS5U'
        )
        db.session.add(user)
    admin_exists = User.query.filter_by(username='admin').first()
    if not admin_exists:
        admin = User(
            username='admin',
            role='admin',
            password='JKSipm0YH'
        )
        db.session.add(admin)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
END

exec "$@"