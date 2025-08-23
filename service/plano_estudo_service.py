from datetime import datetime
from repository.plano_estudo_repository import PlanoEstudoRepository
from models.plano_estudo import PlanoEstudo
from models.enuns import StatusPlanoEstudo


class PlanoEstudoService:

    def __init__(self):
        self.repository = PlanoEstudoRepository()


    def criar(self, dados):
        doc = self.repository.collection.document()
        plano_estudo = PlanoEstudo(
            id = doc.id,
            disciplina = dados["disciplina"],
            descricao = dados["descricao"],
            status = StatusPlanoEstudo.criado.value,
            data_inicio = datetime.now(),
            data_fim = datetime.strptime(dados["data_fim"], "%d/%m/%Y")
        )

        return self.repository.criar(plano_estudo)
    

    def editar(self, id, dados):
        plano = self.repository.listar_por_id(id)

        if not plano:
            return None
        
        plano["descricao"] = dados["descricao"]
        plano["disciplina"] = dados["disciplina"]
        plano["status"] = dados["status"]
        plano["data_fim"] = dados["data_fim"]
        plano = self.repository.editar(id, dados)
        return plano
        
    
    def listar_por_id(self, id):
        return self.repository.listar_por_id(id)
    
    
    def listar(self):
        return self.repository.listar()
    

    def deletar(self, id):
        plano = self.repository.listar_por_id(id)
        if not plano:
            return None
        
        return self.repository.deletar(id)