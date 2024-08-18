import flask
from service import Cadastrar_Usuario

app = flask.Flask(__name__)
app.secret_key = "GeeksForGeeks"

@app.get("/")
def pagina_inicial():
    return flask.render_template("index.html")

@app.get("/cadastrar_usuario")
def pagina_cadastro_usuario():
    return flask.render_template("cadastro_usuario.html")

@app.post("/cadastrar")
def cadastrar():
    input_nome = flask.request.form.get("input_nome")
    input_email = flask.request.form.get("input_email")
    input_senha = flask.request.form.get("input_senha")
    input_confirmar_senha = flask.request.form.get("input_confirmar_senha")

    cadastrar_usuario = Cadastrar_Usuario(nome_usuario=input_nome,
                                          email_usuario=input_email,
                                          senha_usuario=input_senha,
                                          confirmar_senha_usuario=input_confirmar_senha)
    
    return cadastrar_usuario.Cadastrar()