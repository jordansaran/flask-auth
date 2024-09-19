from datetime import timedelta

from flask_jwt_extended import create_access_token
from flask_restx import Namespace, Resource
from werkzeug.security import check_password_hash

from api.src.marshalls import marshall_body_user
from api.src.models.user import User

ns_token = Namespace(
    name="Token",
    description=f"Informações sobre Token de autenticação.",
    validate=True,
    path=f'/token'
)

@ns_token.route("/token")
class Auth(Resource):

    @ns_token.expect(marshall_body_user, validate=True)
    def post(self):
        f"""Obter Token"""
        auth = ns_token.payload
        username = auth.get('username')
        password = auth.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            access_token = create_access_token(
                identity={'username': user.username, 'role': user.role},
                expires_delta=timedelta(hours=1)
            )
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401
