""""Blueprints to API"""
from flask import Blueprint
from flask_restx import Api

from api.src.namespaces.admin import ns_admin
from api.src.namespaces.auth import ns_token
from api.src.namespaces.user import ns_user
from core.settings import Settings

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Coloque o token JWT aqui: Bearer {token}'
    }
}

api_bp_pipeline = Blueprint(name='api', import_name=__name__, url_prefix='/api/v1')
settings = Settings()
api_pipeline = Api(
    api_bp_pipeline,
    version='1.0.0',
    title='Flask Auth - API',
    security='Bearer Auth',
    authorizations=authorizations,
    description='Bem vindo a UI documentacão Flask Auth com Swagger',
    doc='/ui' if Settings().debug_is_enabled() else False,
    validate=True
)

api_pipeline.add_namespace(ns_user)
api_pipeline.add_namespace(ns_token)
api_pipeline.add_namespace(ns_admin)


if not settings.debug_is_enabled():
    api_pipeline.init_app(api_bp_pipeline, add_specs=False)
