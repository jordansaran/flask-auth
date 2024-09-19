from werkzeug.security import generate_password_hash
from api.src.models.mixin import MixinNotAutoIncrement, MixinBase
from app import db


class User(MixinBase):
    __tablename__ = "user"

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

    def __init__(self, username: str, password: str, role: str = 'user'):
        self.username = username
        self.role = role
        self.password = generate_password_hash(password)
