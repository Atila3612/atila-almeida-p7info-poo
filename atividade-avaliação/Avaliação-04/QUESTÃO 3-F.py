#Depência
#Trata-se de uma relação de dependência pois qualquer alteração feita na parte emissora, automaticamente ocorre mudança na parte receptora da mensagem
import time
class envia():
    def enviar(self):
        return time.ctime(time.time()) + "\r\n"

class recebe():
    def __init__(self, param):
        print(param.enviar())

send = envia()
receive = recebe(send)