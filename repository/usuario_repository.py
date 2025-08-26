from config.firebase_config import db


class UsuarioRepository:

    
    def __init__(self):
        self.collection = db.collection("usuarios")


    def criar(self, usuario):
        doc_ref = self.collection.document(usuario.id)
        doc_ref.set(usuario.to_dict())
        return usuario.to_dict()
    

    def listar_usuario_por_email(self, email):
        doc_ref = self.collection.where("email", "==", email).get()
        return doc_ref[0].to_dict() if doc_ref else None


    def listar_usuario_por_id(self, id):
        return self.collection.document(id)