"""Marshall to Namespaces"""
from flask_restx import Model, fields

marshall_body_user = Model("User", {
    'username': fields.String(required=True, description="Nome do usuário"),
    'password': fields.String(required=True, description="Senha"),
})

marshall_user = Model("User", {
    'id': fields.Integer(description="ID "),
    'username': fields.String(description="Nome do usuário"),
    'created_at': fields.DateTime(description="Data de Criação"),
    'updated_at': fields.DateTime(description="Data de Criação"),
})

marshall_api_response = Model("ApiResponse", {
    'code': fields.Integer(readonly=True, description="código"),
    'type': fields.String(readonly=True, description="Tipo de reposta da API"),
    'message': fields.String(readonly=True, description="Mensagem descrevendo a resposta da API"),
})