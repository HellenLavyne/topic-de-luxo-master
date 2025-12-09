import unittest

from src.passageiro import Passageiro
from src.topic import Topic


class TestTopic(unittest.TestCase):

    def testInicializacao(self):
        topic = Topic(10, 2)
        self.assertEqual(8, topic.getNumeroAssentosNormais(), "Quantidade errada de assentos comuns!")
        self.assertEqual(2, topic.getNumeroAssentosPrioritarios(), "Quantidade errada de assentos prioritários!")

#    def testQdtPrioritariosMaiorCapacidade(self):
#        with self.assertRaises(ValueError) as context:
#            topic = Topic(5, 10)

#        self.assertEqual(str(context.exception), "Não foi retornado um erro do tipo ValueErrorException!")
#        self.assertThrows(IllegalArgumentException.class ,() -> {new Topic(5, 10);}, "Não foi retornado um erro do tipo IllegalArgumentException!")

    def testPassageiroPrioriatioComVagaPrioritaria(self):
        topic = Topic(2, 1)
        self.assertTrue(topic.subir(Passageiro("Marlus", 120)), "A topic tem vaga mas o passageiro não foi inserido!")
        self.assertTrue(topic.subir(Passageiro("Eduarda", 19)), "A topic tem vaga mas o passageiro não foi inserido!")
        eduarda = topic.getPassageiroAssentoNormal(0)
        marlus = topic.getPassageiroAssentoPrioritario(0)
        self.assertIsNotNone(marlus, "Falha na inserção!")
        self.assertEqual("Marlus", marlus.getNome(), "Passageiro errado")
        self.assertIsNotNone(eduarda, "Falha na inserção!")
        self.assertEqual("Eduarda", eduarda.getNome(), "Passageiro errado")

    def testPassageiroSemPrioridadeComVagaComum(self):
        topic = Topic(2, 1)
        self.assertTrue(topic.subir(Passageiro("Eduarda", 19)), "A topic tem vaga mas o passageiro não foi inserido!")
        self.assertTrue(topic.subir(Passageiro("Marlus", 120)), "A topic tem vaga mas o passageiro não foi inserido!")
        eduarda = topic.getPassageiroAssentoNormal(0)
        self.assertIsNotNone(eduarda, "Falha na inserção!")
        self.assertEqual("Eduarda", eduarda.getNome(), "Passageiro sem prioridade nao encontrado")

    def testPassageiroPrioriatioSemVagaPrioritaria(self):
        topic = Topic(2, 1)
        self.assertTrue(topic.subir(Passageiro("Eduarda", 190)), "A topic tem vaga mas o passageiro não foi inserido!")
        self.assertTrue(topic.subir(Passageiro("Guthyerri", 120)), "Tinha uma vaga comum pro idoso ocupar!")
        guthyerri = topic.getPassageiroAssentoNormal(0)
        self.assertIsNotNone(guthyerri, "Passageiro nao encontrado")
        self.assertEqual("Guthyerri", guthyerri.getNome(), "Passageiro com prioridade nao encontrado")

    def testPassageiroSemPrioriadadeSemVagaComum(self):
        topic = Topic(2, 1)
        self.assertTrue(topic.subir(Passageiro("Eduarda", 19)), "A topic tem vaga mas o passageiro não foi inserido!")
        self.assertTrue(topic.subir(Passageiro("Guthyerri", 19)), "Tinha assento prioritário vago pra ele sentar!")
        guthyerri = topic.getPassageiroAssentoPrioritario(0)
        self.assertIsNotNone(guthyerri, "Passageiro nao encontrado")
        self.assertEqual("Guthyerri", guthyerri.getNome(), "Passageiro com prioridade nao encontrado")

    def testDescidaTopicVazia(self):
        topic = Topic(2, 1)
        self.assertFalse(topic.descer("Joaquim"), "Removeu alguém sendo que a topic está vazia!")

    def testDescidaDePassageiro(self):
        topic = Topic(2, 1)
        topic.subir(Passageiro("Guthyerri", 19))
        self.assertTrue(topic.descer("Guthyerri"), "Falha ao remover!")
        guthyerri = topic.getPassageiroAssentoNormal(0)
        self.assertIsNone(guthyerri, "O passageiro nao foi removido")
        self.assertEqual(2, topic.getVagas(), "Removeu uma posição do array, deveria somente setar como null!!!")

    def testDescerPassageiroNaoSubiu(self):
        topic = Topic(2, 1)
        topic.subir(Passageiro("Guthyerri", 19))
        topic.descer("Guthyerri")
        self.assertFalse(topic.descer("Zé Adolfo"), "Removeu alguém que não estava na topic!")

    def testCapacidade(self):
        topic = Topic(2, 1)
        topic.subir(Passageiro("Marlus", 12))
        topic.subir(Passageiro("Guthyerri", 130))
        self.assertFalse(topic.subir(Passageiro("Hermilson", 16)), "Tamanho da Topic foi estourado!")

    def testMostrarVagas(self):
        topic = Topic(5, 3)
        self.assertEqual(5, topic.getVagas(), "Quantidade de vagas disponíveis está errada!")
        topic.subir(Passageiro("Bode", 5))
        self.assertEquals(4, topic.getVagas(), "Quantidade de vagas disponíveis está errada!")

    def testMostrarTopicVazia(self):
        topic = Topic(10, 5)
        self.assertEqual("[@ @ @ @ @ = = = = =]", topic.toString(), "Sua lista está errada!")

    def testMostrarTopicCheia(self):
        topic = Topic(10, 5)
        topic.subir(Passageiro("Marlus", 120))
        topic.subir(Passageiro("Eduarda", 19))
        topic.subir(Passageiro("Guthyerri", 19))
        self.assertEqual("[@Marlus @ @ @ @ =Eduarda =Guthyerri = = =]", topic.toString(),
                         "Sua lista está com impressão errada!")


if __name__ == '__main__':
    unittest.main()
