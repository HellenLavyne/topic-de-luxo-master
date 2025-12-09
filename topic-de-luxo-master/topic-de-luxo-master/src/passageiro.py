class Passageiro:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def ePrioridade(self):
        # O passageiro é idoso se a idade for >= 65, o que confere prioridade.
        return self.idade >= 65

    def getNome(self):
        return self.nome