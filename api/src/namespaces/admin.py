from http import HTTPStatus
from logging import error
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, marshal
from api.src.constants import StatusAPI
from api.src.decorators import exceptions, role_required
from api.src.marshalls import marshall_body_user, marshall_api_response, marshall_user
from api.src.models.user import User
from app import db

model = "Admin"

ns_admin = Namespace(
    name=model,
    description=f"Informações sobre {model}.",
    validate=True,
    path=f'/{model.lower()}'
)
ns_admin.models.update({marshall_body_user.name: marshall_body_user})
ns_admin.models.update({marshall_api_response.name: marshall_api_response})


@ns_admin.route("/<int:id>/")
@ns_admin.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR),
    'Erro de conexão com o servidor.',
    marshall_api_response
)
@ns_admin.response(
    int(HTTPStatus.UNAUTHORIZED),
    'Não autorizado',
    marshall_api_response
)
@ns_admin.response(
    int(HTTPStatus.BAD_REQUEST),
    'Ocorreu um erro',
    marshall_api_response
)
@ns_admin.response(
    int(HTTPStatus.ACCEPTED),
    f"{model} encontrado com sucesso.",
    marshall_user
)
class AdminNamespace(Resource):
    f"""Handles HTTP requests to url: /{model} by Body"""

    @jwt_required()
    @role_required('admin')
    @exceptions(ns_admin)
    def get(self, id: int = None):
        f"""Obter dados do {model} a partir do ID"""
        user = User.get_by_id(id)
        if user is not None:
            return marshal(user.to_dict(), marshall_user), int(HTTPStatus.ACCEPTED)
        return (marshal(
            StatusAPI.REQUEST_NOT_FOUND_API, marshall_api_response),
                int(HTTPStatus.NOT_FOUND)
        )


@ns_admin.route("")
@ns_admin.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR),
    'Erro de conexão com o servidor.',
    marshall_api_response
)
@ns_admin.response(
    int(HTTPStatus.UNAUTHORIZED),
    'Não autorizado'
)
@ns_admin.response(
    int(HTTPStatus.BAD_REQUEST),
    'Ocorreu um erro',
    marshall_api_response
)
@ns_admin.response(
    int(HTTPStatus.CREATED),
    f'Cadastro do {model} realizado com sucesso',
    marshall_api_response
)
@ns_admin.response(
    int(HTTPStatus.ACCEPTED),
    f"Lista de {model} encontrado com sucesso.",
    marshall_user
)
class AdminByBody(Resource):
    f"""Handles HTTP requests to url: /{model} by Body"""

    @jwt_required()
    @role_required('admin')
    @ns_admin.marshal_list_with(marshall_user)
    def get(self):
        f"""Retornar lista de {model}"""
        return User.query.filter_by(role='admin').all()


    @jwt_required()
    @role_required('admin')
    @exceptions(ns_admin)
    @ns_admin.expect(marshall_body_user, validate=True)
    def post(self):
        f"""Processo de cadastro de {model}"""
        payload = ns_admin.payload
        payload['role'] = 'admin'
        user = User(**payload).insert()
        if user:
            try:
                db.session.commit()
                return (marshal(
            StatusAPI.REQUEST_SUCCESS_API, marshall_api_response),
                int(HTTPStatus.CREATED)
                )
            except Exception as _error:
                error(_error)
        return (marshal(
            StatusAPI.BAD_REQUEST_API, marshall_api_response),
                int(HTTPStatus.BAD_REQUEST)
            )
