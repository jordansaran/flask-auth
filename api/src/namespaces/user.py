from http import HTTPStatus
from logging import error, debug
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, marshal
from api.src.constants import StatusAPI
from api.src.decorators import exceptions
from api.src.marshalls import marshall_body_user, marshall_api_response, marshall_user
from api.src.models.user import User
from api.src.utils import httpstatus_to_api_response
from app import db

model = "User"

ns_user = Namespace(
    name=model,
    description=f"Informações sobre {model}.",
    validate=True,
    path=f'/{model}'
)
ns_user.models.update({marshall_body_user.name: marshall_body_user})
ns_user.models.update({marshall_api_response.name: marshall_api_response})


@ns_user.route("/<int:id>/")
@ns_user.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR),
    'Erro de conexão com o servidor.',
    marshall_api_response
)
@ns_user.response(
    int(HTTPStatus.UNAUTHORIZED),
    'Não autorizado',
    marshall_api_response
)
@ns_user.response(
    int(HTTPStatus.BAD_REQUEST),
    'Ocorreu um erro',
    marshall_api_response
)
@ns_user.response(
    int(HTTPStatus.ACCEPTED),
    f"{model} encontrado com sucesso.",
    marshall_user
)
class UserNamespace(Resource):
    f"""Handles HTTP requests to url: /{model} by Body"""

    @jwt_required()
    @exceptions(ns_user)
    def get(self, id: int = None):
        f"""Obter dados do {model} a partir do ID"""
        user = User.get_by_id(id)
        if user is not None:
            return marshal(user.to_dict(), marshall_user), int(HTTPStatus.ACCEPTED)
        return (marshal(
            StatusAPI.REQUEST_NOT_FOUND_API, marshall_api_response),
                int(HTTPStatus.NOT_FOUND)
        )


@ns_user.route("")
@ns_user.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR),
    'Erro de conexão com o servidor.',
    marshall_api_response
)
@ns_user.response(
    int(HTTPStatus.UNAUTHORIZED),
    'Não autorizado'
)
@ns_user.response(
    int(HTTPStatus.BAD_REQUEST),
    'Ocorreu um erro',
    marshall_api_response
)
@ns_user.response(
    int(HTTPStatus.CREATED),
    f'Cadastro do {model} realizado com sucesso',
    marshall_api_response
)
@ns_user.response(
    int(HTTPStatus.ACCEPTED),
    f"Lista de {model} encontrado com sucesso.",
    marshall_user
)
class UserByBody(Resource):
    f"""Handles HTTP requests to url: /{model} by Body"""

    @jwt_required()
    @ns_user.marshal_list_with(marshall_user)
    def get(self):
        f"""Retornar lista de {model}"""
        return User.query.all()

    @ns_user.expect(marshall_body_user, validate=True)
    @exceptions(ns_user)
    def post(self):
        f"""Processo de cadastro de {model}"""
        payload = ns_user.payload
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
        return marshal(httpstatus_to_api_response((
            400,
            'Bad Request',
            ''
        )), marshall_api_response), \
            int(HTTPStatus.BAD_REQUEST)
