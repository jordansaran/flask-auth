<p align="center">
    <h2 align="center">
        Flasth Auth - API
    </h2>
    <a href="https://github.com/jordansaran/flask-auth/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/jordansaran/flask-auth?color=0088ff" />
    </a>
    <a href="https://github.com/jordansaran/flask-auth/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/jordansaran/flask-auth?color=0088ff" />
    </a>
</p>

Foi desenvolvido uma API onde seu objetivo é realizar a autenticação de usuários. Neste caso existe dois tipos de usuários, sendo eles:
- Usário comum
- Usuário administrador

# 1.Instalação
Certifique-se de utilizar a última versão do código fonte, que normalmente fica na branch "main"(principal) do repositório do github.
Logo abaixo é apresentado opções de instalação de ambiente, sendo:
1. Ambiente Virtual(env)
2. Docker

````shell
# clone o repositório
$ git clone https://github.com/jordansaran/flask-auth.git
$ cd flask-auth
````

## 1.1. Criar ambiente virtual
Crie um virtualenv em ambiente Unix e ative-o:
````shell
$ python3 -m venv venv
$ . venv/bin/activate
````
Ou no Windows cmd:
````shell
$ python3 -m venv venv
$ venv\Scripts\activate.bat
````
Instalando bibliotecas e suas dependências realcionados a API.  
````shell
$ pip install -r requirements.txt
````

## 1.2. Docker

Para replicar o ambiente de desenvolvimento e colocar em execução a API, execute o comando logo abaixo. 
Destacando que é necessário que seu ambiente de desenvolvimento possua [**Docker**](https://www.docker.com/products/docker-desktop/) instalado.
```
docker-compose up flask-auth
```
### Observações
A url de acesso a API é **http://127.0.0.1:8000/**, caso deseje alterar a porta de acesso modifique
o arquivo **docker-compose.yml** no parametro **ports** (8000:8000) e o arquivo **Dockerfile** na linha 28 referente ao EXPOSE.

# 2. Inicializar API
Antes de executar a API crie um arquivo **.env** na raiz do projeto caso ele não tenha sido criado, para servir de referência
o arquivo **.env.example** demonstra a estrutura necessário para o arquivo **.env**.
O arquivo deve conter os seguintes variáveis de ambiente.
````dotenv
SECRET_KEY=
JWT_SECRET_KEY=
FLASK_DEBUG=1
FLASK_APP=app.py
SQLALCHEMY_DATABASE_URI=postgresql://postgres:postgres@db:5432/postgres
SQLALCHEMY_TRACK_MODIFICATIONS=0
RESTX_MASK_SWAGGER=False
RESTX_VALIDATE=True
ENVIRONMENT=Development
````
A variável **SECRET_KEY** deve conter um hash que será utilizado quando a API for utilizada em **production**.
A variável **DEBUG** deve possuir os valores 1 ou 0 para referenciar a condição de **True** ou **False** para
executar aplicação em modo **DEBUG**.
A variável **JWT_SECRET_KEY** é utilizada para autenticação JWT, então é crucial que você passa a chave de criptografia.
A variável **SQLALCHEMY_DATABASE_URI** é utilizada para conexação com o banco de dados em formato de string, como demonstrado acima.
Dentro do projeto existe um arquivo **.env.example** que contém um exemplo com os valores respectivos a cada variável, você pode 
copiar o conteúdo desse arquivo para dentro do arquivo **.env**
## 2.1. Docker
Apenas execute o seguinte comando para inicializar o container da aplicação via terminal ou IDE para inseir os seeders dentro do banco de dados.
````shell
docker-compose start flask-auth
````

# Documentação

Abra http://localhost:8000/ em seu navegador para acessar a documentação da API.
Caso deseje visualizar outra forma de documentação. Esse endpoint só visível caso a variável ambiente **FLASK_DEBUG** esteja com o valor igual a 1, 
caso não esteja, a rota não se encontrada.
1. http://localhost:8000/api/v1/ui
