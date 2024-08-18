import flask
import hashlib as hl
import re
import requests
from error import Campo_Cadastro_Vazio, Campo_Cadastro_Nome_Curto, Campo_Cadastro_Nome_Longo, Campo_Cadastro_Senha_Curta, Campo_Cadastro_Senhas_Diferentes, Campo_Cadastro_Email_Inexistente, Campo_Cadastro_Email_Ja_Cadastrado

class Cadastrar_Usuario(object):
    def __init__(self, nome_usuario, email_usuario, senha_usuario, confirmar_senha_usuario) -> None:
        self.nome_usuario = nome_usuario
        self.email_usuario = email_usuario
        self.senha_usuario = senha_usuario
        self.confirmar_senha_usuario = confirmar_senha_usuario

        self.senha_hash = (lambda senha: hl.md5(b'%s' %bytes(senha.encode())).hexdigest())

        self.verificar_email = (lambda email: re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) == None)

        self.usuarios = requests.get("http://127.0.0.1:8000/")

        self.usuarios_json = self.usuarios.json()
    
    def Cadastrar(self):
        try:
            if self.nome_usuario == "" or self.email_usuario == "" or self.senha_usuario == "" or self.confirmar_senha_usuario == "":
                raise Campo_Cadastro_Vazio
            elif len(self.nome_usuario) < 8:
                raise Campo_Cadastro_Nome_Curto
            elif len(self.nome_usuario) > 25:
                raise Campo_Cadastro_Nome_Longo
            elif self.verificar_email(self.email_usuario):
                raise Campo_Cadastro_Email_Inexistente
            elif self.email_usuario in self.usuarios_json:
                raise Campo_Cadastro_Email_Ja_Cadastrado
            elif len(self.senha_usuario) < 6:
                raise Campo_Cadastro_Senha_Curta
            elif self.senha_usuario != self.confirmar_senha_usuario:
                raise Campo_Cadastro_Senhas_Diferentes

        except Campo_Cadastro_Vazio:
            flask.flash("Algum campo não foi preencido")
            flask.flash(self.nome_usuario)
            flask.flash(self.email_usuario)
            flask.flash(self.senha_usuario)
            flask.flash(self.confirmar_senha_usuario)

            return flask.redirect(flask.request.referrer)
        except Campo_Cadastro_Nome_Curto:
            flask.flash("O Nome está muito curto")
            flask.flash(self.nome_usuario)
            flask.flash(self.email_usuario)
            flask.flash(self.senha_usuario)
            flask.flash(self.confirmar_senha_usuario)

            return flask.redirect(flask.request.referrer)
        except Campo_Cadastro_Nome_Longo:
            flask.flash("O Nome está muito longo")
            flask.flash(self.nome_usuario)
            flask.flash(self.email_usuario)
            flask.flash(self.senha_usuario)
            flask.flash(self.confirmar_senha_usuario)

            return flask.redirect(flask.request.referrer)
        except Campo_Cadastro_Senha_Curta:
            flask.flash("A Senha está curta")
            flask.flash(self.nome_usuario)
            flask.flash(self.email_usuario)
            flask.flash(self.senha_usuario)
            flask.flash(self.confirmar_senha_usuario)

            return flask.redirect(flask.request.referrer)
        except Campo_Cadastro_Senhas_Diferentes:
            flask.flash("As senhas estão diferentes")
            flask.flash(self.nome_usuario)
            flask.flash(self.email_usuario)
            flask.flash(self.senha_usuario)
            flask.flash(self.confirmar_senha_usuario)

            return flask.redirect(flask.request.referrer)
        except Campo_Cadastro_Email_Inexistente:
            flask.flash("E-mail não existente")
            flask.flash(self.nome_usuario)
            flask.flash(self.email_usuario)
            flask.flash(self.senha_usuario)
            flask.flash(self.confirmar_senha_usuario)

            return flask.redirect(flask.request.referrer)
        except Campo_Cadastro_Email_Ja_Cadastrado:
            flask.flash("E-mail já cadastrado")
            flask.flash(self.nome_usuario)
            flask.flash(self.email_usuario)
            flask.flash(self.senha_usuario)
            flask.flash(self.confirmar_senha_usuario)

            return flask.redirect(flask.request.referrer)
        else:
            requests.post(f"http://127.0.0.1:8000/cadastrar-usuario/{self.nome_usuario}/{self.email_usuario}/{self.senha_hash(self.senha_usuario)}")
           
            return "cadastrado"
        
            