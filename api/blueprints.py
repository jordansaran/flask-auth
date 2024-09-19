""""Blueprints to API"""
from flask import Blueprint
from flask_restx import Api
from core.settings import Settings


api_bp_pipeline = Blueprint(name='api', import_name=__name__, url_prefix='/api/v1')
settings = Settings()
api_pipeline = Api(
    api_bp_pipeline,
    version='1.0.0',
    title='Flask Auth - API',
    description='Bem vindo a UI documentacão Flask Auth com Swagger',
    doc='/ui' if Settings().debug_is_enabled() else False,
    validate=True
)

if not settings.debug_is_enabled():
    api_pipeline.init_app(api_bp_pipeline, add_specs=False)
