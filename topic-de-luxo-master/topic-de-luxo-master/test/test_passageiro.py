import unittest

from src.passageiro import Passageiro


class TestPassageiro (unittest.TestCase):

    def testTruePriority(self):
        passageiro = Passageiro("Guthyerri", 160)
        self.assertTrue(passageiro.ePrioridade(), "O passageiro é prioridade")  # add assertion here

    def testFalsePriority(self):
        passageiro = Passageiro("Guthyerri", 19)
        self.assertFalse(passageiro.ePrioridade(), "O passageiro é prioridade")  # add assertion here


if __name__ == '__main__':
    unittest.main()
