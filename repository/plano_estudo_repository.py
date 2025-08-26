from config.firebase_config import db
from repository.usuario_repository import UsuarioRepository

class PlanoEstudoRepository:


    def __init__(self):
        self.collection = db.collection("planos_estudos")
        self.usuario_repository = UsuarioRepository()


    def criar(self, plano, usuario_id):
        usuario_ref = self.usuario_repository.listar_usuario_por_id(usuario_id)
        plano_ref = usuario_ref.collection("planos_estudos").document(plano.id)
        plano_ref.set(plano.to_dict())
        return plano.to_dict()

    
    def editar(self, id, usuario_id, plano):
        usuario_ref = self.usuario_repository.listar_usuario_por_id(usuario_id)
        doc_ref = usuario_ref.collection("planos_estudos").document(id)
        doc_ref.update(plano)
        return doc_ref.get()
    

    def listar_por_id(self, id, usuario_id):
        usuario_ref = self.usuario_repository.listar_usuario_por_id(usuario_id)
        doc = usuario_ref.collection("planos_estudos").document(id).get()
        return doc.to_dict() if doc.exists else None
    

    def listar(self, usuario_id):
        usuario_ref = self.usuario_repository.listar_usuario_por_id(usuario_id)
        docs = usuario_ref.collection("planos_estudos").stream()
        return [doc.to_dict() for doc in docs]
    

    def deletar(self, id, usuario_id):
        usuario_ref = self.usuario_repository.listar_usuario_por_id(usuario_id)
        doc = usuario_ref.collection("planos_estudos").document(id)
        doc.delete()
        return True