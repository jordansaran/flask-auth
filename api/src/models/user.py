from werkzeug.security import generate_password_hash

from api.src.models.mixin import MixinNotAutoIncrement
from app import db


class User(MixinNotAutoIncrement):
    username = db.Column(
        db.String(80),
        unique=True
    )
    role = db.Column(
        db.String(10)
    )
    password = db.Column(
        db.String(256)
    )

    def __init__(self, username, role, password_hash):
        self.username = username
        self.role = role
        self.password = generate_password_hash(password_hash)
