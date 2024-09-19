"""Settings env"""
import ast
import logging
from os import getenv
from os.path import join, exists
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent


class Env:
    """
    Class para criação de env para configuração do Flask
    """
    _dotenv_path = join(BASE_DIR, '.env')
    _debug: bool = True

    def __init__(self):
        """
        Get informações sobre o arquivo .env
        """
        load_dotenv(dotenv_path=self._dotenv_path)
        if exists(self._dotenv_path):
            self.ENVIRONMENT = getenv('ENVIRONMENT', "Development")
            self.SECRET_KEY = getenv('SECRET_KEY', "")
            self.FLASK_DEBUG = getenv('FLASK_DEBUG', "1")
            self._debug = bool(self.FLASK_DEBUG)
            self.FLASK_APP = getenv('FLASK_APP', "")
            self.RESTX_MASK_SWAGGER = False
            self.RESTX_VALIDATE = True
            self.SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI', "")
            self.SQLALCHEMY_BINDS = ast.literal_eval(getenv('SQLALCHEMY_BINDS', "{}"))
            self.SQLALCHEMY_TRACK_MODIFICATIONS = bool(
                getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "0")
            )
            self.__to_verify()
        else:
            raise FileNotFoundError("Arquivo .env não encontrado, crie um arquivo na raiz do projeto.")

    def get_environment(self):
        return self.ENVIRONMENT

    def __to_verify(self):
        if not self._debug:
            if len(self.SECRET_KEY) == 0:
                raise ValueError("A secret key não pode ser vazia, inclua uma secret key.")
        if len(self.FLASK_APP) == 0:
            raise ValueError("A variável FLASK_APP não pode ser vazio. Inclua um arquivo.")

    def debug_is_enabled(self) -> bool:
        """
        Verifica se DEBUG está habilitado no env
        :return: bool
        """
        return self._debug


class Settings(Env):

    def __init__(self):
        Env.__init__(self)
        logging.basicConfig(level=logging.DEBUG if self._debug else logging.WARNING)
