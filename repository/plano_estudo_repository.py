from config.firebase_config import db


class PlanoEstudoRepository:


    def __init__(self):
        self.collection = db.collection("estudos")


    def criar(self, plano):
        doc_ref = self.collection.document(plano.id)
        doc_ref.set(plano.to_dict())
        return plano.to_dict()