from config.firebase_config import db


class PlanoEstudoRepository:


    def __init__(self):
        self.collection = db.collection("estudos")


    def criar(self, plano):
        doc_ref = self.collection.document(plano.id)
        doc_ref.set(plano.to_dict())
        return plano.to_dict()

    
    def editar(self, id, plano):
        doc_ref = self.collection.document(id)
        doc_ref.update(plano)
        return doc_ref.get()
    

    def listar_por_id(self, id):
        doc = self.collection.document(id).get()
        return doc.to_dict() if doc.exists else None
    

    def listar(self):
        docs = self.collection.stream()
        return [doc.to_dict() for doc in docs]
    

    def deletar(self, id):
        doc = self.collection.document(id)
        doc.delete()
        return True