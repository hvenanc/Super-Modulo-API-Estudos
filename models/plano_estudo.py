from models.enuns import StatusPlanoEstudo


class PlanoEstudo:


    def __init__(self, id, disciplina, descricao, status: StatusPlanoEstudo, data_inicio, data_fim):
        self.id = id
        self.disciplina = disciplina
        self.descricao = descricao
        self.status = status if isinstance(status, StatusPlanoEstudo) else StatusPlanoEstudo(status)
        self.data_inicio = data_inicio
        self.data_fim = data_fim


    def to_dict(self):
        return {
            "id": self.id,
            "disciplina": self.disciplina,
            "descricao": self.descricao,
            "status": self.status.value,
            "data_inicio": self.data_inicio,
            "data_fim": self.data_fim
        }