import flask
import hashlib as hl
import requests
from error import Campo_Vazio, Campo_Email_Incorreto, Campo_Senha_Incorreta

class Logar_Usuario(object):
    def __init__(self, email_usuario, senha_usuario) -> None:
        self.email_usuario = email_usuario
        self.senha_usuario = senha_usuario

        self.senha_hash = (lambda senha: hl.md5(b'%s' %bytes(senha.encode())).hexdigest())

        self.usuarios = requests.get(f"http://127.0.0.1:8000/filtrar-usuario/{self.email_usuario}")

        self.usuarios_json = self.usuarios.json()
    
    def Logar(self):
        print(self.usuarios_json)
        try:
            if self.email_usuario == "" or self.senha_usuario == "":
                raise Campo_Vazio
            elif self.usuarios_json == []:
                raise Campo_Email_Incorreto
            elif self.senha_hash(self.senha_usuario) != self.usuarios_json[0][2]:
                raise Campo_Senha_Incorreta
        
        except Campo_Vazio:
            flask.flash("Algum campo não foi preencido")
            
            return flask.redirect(flask.request.referrer)
        except Campo_Email_Incorreto:
            flask.flash("E-mail incorreto")
            
            return flask.redirect(flask.request.referrer)
        except Campo_Senha_Incorreta:
            flask.flash("Senha incorreta")
            
            return flask.redirect(flask.request.referrer)
        else:
            return "entrou"
        