from src.passageiro import Passageiro
from src.topic import Topic

if __name__ == '__main__':
    topic = Topic(5, 2)
    print(topic.__dict__)

    passageiro = Passageiro('davi', 17)
    topic.subir(passageiro)
    print(topic.__dict__)

    passageiro = Passageiro('joao', 103)
    topic.subir(passageiro)
    print(topic.__dict__)

    passageiro = Passageiro('ana', 35)
    topic.subir(passageiro)
    print(topic.__dict__)

    passageiro = Passageiro('rex', 20)
    topic.subir(passageiro)
    passageiro = Passageiro('bia', 16)
    topic.subir(passageiro)
    print(topic.__dict__)

    topic.descer("davi")
    print(topic.__dict__)

    passageiro = Passageiro('aragao', 96)
    topic.subir(passageiro)
    print(topic.__dict__)

    passageiro = Passageiro('lucas', 23)
    if topic.subir(passageiro) is False:
        print("Topic lotada")

    if topic.descer("marcelo") is False:
        print("Passageiro nao esta na topic")

    topic.descer("ana")

    passageiro = Passageiro('bia', 16)
    if topic.subir(passageiro) is False:
        print("Passageiro ja esta na topic")


    print(topic.__dict__)
