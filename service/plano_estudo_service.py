from datetime import datetime
from repository.plano_estudo_repository import PlanoEstudoRepository
from models.plano_estudo import PlanoEstudo
from models.enuns import StatusPlanoEstudo


class PlanoEstudoService:

    def __init__(self):
        self.repository = PlanoEstudoRepository()


    def criar(self, dados, usuario_id):
        doc = self.repository.collection.document()
        plano_estudo = PlanoEstudo(
            id = doc.id,
            disciplina = dados["disciplina"],
            descricao = dados["descricao"],
            status = StatusPlanoEstudo.criado.value,
            data_inicio = datetime.now(),
            data_fim = datetime.strptime(dados["data_fim"], "%d/%m/%Y")
        )

        return self.repository.criar(plano_estudo, usuario_id)
    

    def editar(self, id, usuario_id, dados):
        plano = self.repository.listar_por_id(id, usuario_id)

        if not plano:
            return None
        
        plano["descricao"] = dados["descricao"]
        plano["disciplina"] = dados["disciplina"]
        plano["status"] = dados["status"]
        plano["data_fim"] = dados["data_fim"]
        plano = self.repository.editar(id, usuario_id, dados)
        return plano.to_dict()
        
    
    def listar_por_id(self, id, usuario_id):
        return self.repository.listar_por_id(id, usuario_id)
    
    
    def listar(self, usuario_id):
        return self.repository.listar(usuario_id)
    

    def deletar(self, id, usuario_id):
        plano = self.repository.listar_por_id(id, usuario_id)
        if not plano:
            return None
        
        return self.repository.deletar(id, usuario_id)