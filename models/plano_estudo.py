from enuns import StatusPlanoEstudo


class PlanoEstudo:


    def __init__(self, id, disciplina, descricao, status: StatusPlanoEstudo, data_inicio, data_fim):
        self.id = id
        self.disciplina = disciplina
        self.descricao = descricao
        self.status = isinstance(status, StatusPlanoEstudo) if self.status == status else self.status = StatusPlanoEstudo(status)
        self.data_inicio = data_inicio
        self.data_fim = data_fim


    def to_dict(self, id):
        return {
            "id": str(id),
            "disciplina": self.disciplina,
            "descricao": self.descricao,
            "status": self.status,
            "data_inicio": self.data_inicio,
            "data_fim": self.data_fim
        }