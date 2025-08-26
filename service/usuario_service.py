from werkzeug.security import generate_password_hash
from repository.usuario_repository import UsuarioRepository
from models.usuario import Usuario


class UsuarioService:

    def __init__(self):
        self.repository = UsuarioRepository()


    def criar(self, dados):
        usuario_check = self.repository.listar_usuario_por_email(dados["email"])
        if usuario_check:
            return None
        doc = self.repository.collection.document()
        usuario = Usuario(
            id = doc.id,
            nome = dados["nome"],
            email = dados["email"],
            senha = generate_password_hash(dados["senha"])
        )
        return self.repository.criar(usuario)
    

    def autenticar(self, dados):
        usuario_busca = self.repository.listar_usuario_por_email(dados["email"])
        usuario = Usuario.to_user(usuario_busca)
        if usuario and usuario.check_hash_senha(dados["senha"]):
            return usuario
        else:
            None