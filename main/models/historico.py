from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

    def transacoes_do_dia(self):
        hoje = datetime.now().date()
        return [t for t in self._transacoes if t['data'].date() == hoje]