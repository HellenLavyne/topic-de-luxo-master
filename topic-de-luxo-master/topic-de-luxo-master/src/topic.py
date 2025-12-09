from src.passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios: int):
        if qtdPrioritarios > capacidade:
            raise ValueError("Não pode haver mais assentos prioritários do que a capcidade totl da Topic.")

        # Inicializando assentos prioritários e normais
        num_normais = capacidade - qtdPrioritarios
        self.assentos_prioritarios = [None] * qtdPrioritarios
        self.assentos_normais = [None] * num_normais

    def getNumeroAssentosPrioritarios(self):
        return len(self.assentos_prioritarios)

    def getNumeroAssentosNormais(self):
        return len(self.assentos_normais)

    def getPassageiroAssentoNormal(self, lugar):
        # Verifica se o índice é válido e retorna o passageiro
        if 0 <= lugar < self.getNumeroAssentosNormais():
            return self.assentos_normais[lugar]
        return None

    def getPassageiroAssentoPrioritario(self, lugar):
        if 0 <= lugar < self.getNumeroAssentosPrioritarios():
            return self.assentos_prioritarios[lugar]
        return None

    def getVagas(self):
        # Retorna a soma de vagas livres nos assentos prioritários e normais.
        vagas_prioritarias = self.assentos_prioritarios.count(None)
        vagas_normais = self.assentos_normais.count(None)
        return vagas_prioritarias + vagas_normais

    def _getPrimeiraVaga(self, lista):
        # Método auxiliar para encontrar o primeiro índice vazio (None) em uma lista
        try:
            return lista.index(None)
        except ValueError:
            return -1  # Não há vaga (None não encontrado)

    def _passageiroJaEstaNaTopic(self, nome):
        for passageiro in self.assentos_prioritarios:
            if passageiro and passageiro.getNome() == nome:
                return True
        for passageiro in  self.assentos_normais:
            if passageiro and passageiro.getNome() == nome:
                return True
        return False

    def subir(self, passageiro: Passageiro):
        # Verifica se já está na topic
        if self._passageiroJaEstaNaTopic(passageiro.getNome()):
            return False

        # Verifica se a topic está lotada
        if self.getVagas() == 0:
            return False

        vaga_prioritaria = self._getPrimeiraVaga(self.assentos_prioritarios)
        vaga_normal = self._getPrimeiraVaga(self.assentos_normais)

        if passageiro.ePrioridade():
            # Passageiro idoso (prioritário)
            if vaga_prioritaria != -1:
                self.assentos_prioritarios[vaga_prioritaria] = passageiro
                return True
            elif vaga_normal != -1:
                self.assentos_normais[vaga_normal] = passageiro
                return True
        else:
            # Passageiro não idoso
            if vaga_normal != -1:
                self.assentos_normais[vaga_normal] = passageiro
                return True
            elif vaga_prioritaria != -1:
                self.assentos_prioritarios[vaga_prioritaria] = passageiro
                return True
        return False

    def descer(self, nome):
        # Tenta remover dos assentos prioritários
        for i, passageiro in enumerate(self.assentos_prioritarios):
            if passageiro and passageiro.getNome() == nome:
                self.assentos_prioritarios[i] = None
                return True

        # Tenta remover dos normais
        for i, passageiro in enumerate(self.assentos_normais):
            if passageiro and passageiro.getNome() == nome:
                self.assentos_normais[i] = None
                return True
        # Se o passageiro não foi encontrado em nenhuma lista
        return False

    def toString(self):
        # Colocando @ na frente das cadeiras preferenciais.
        # Colocando = na frente das cadeiras normais.
        assentos_str = []

        # Formata assentos prioritários
        for passageiro in self.assentos_prioritarios:
            if passageiro:
                assentos_str.append(f"@{passageiro.getNome()}")
            else:
                assentos_str.append("@")

        # Formata assentos normais
        for passageiro in self.assentos_normais:
            if passageiro:
                assentos_str.append(f"={passageiro.getNome()}")
            else:
                assentos_str.append("=")

        # Retorna o estado da topic no formato "[item1 item2 ...]"
        return f"[{' '.join(assentos_str)}]"

