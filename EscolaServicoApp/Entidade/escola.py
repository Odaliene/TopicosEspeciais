class Escola(object):
    """docstring forEscola."""

    def __init__(self, id, nome, logradouro, cidade):
        super(Escola, self).__init__()
        self.id = id
        self.nome = nome
        self.cidade = cidade
