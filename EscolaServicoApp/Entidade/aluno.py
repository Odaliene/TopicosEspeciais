class Aluno(object):
    """docstring forAluno."""

    def __init__(self, id, nome, nascimento, matricula, cpf):
        super(Aluno, self).__init__()
        self.id = id
        self.nome = nome
        self.nascimento = nascimento
        self.matricula = matricula
        self.cpf = cpf
