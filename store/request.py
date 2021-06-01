import requests

#Classe do modulo request.
# self.base_url = url padrão pra passar nas funções.class
# self.session = criar uma sessão pra poder usar o get, post e afins.
class Request:
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.session = requests.Session()
    
    #Obter informações em uma url mais seu complemento.
    def get(self, url, **kwargs):
        return self.session.get(self.base_url + url, **kwargs)
    
    #Postar informações em uma url mais seu complemento.
    def post(self, url, **kwargs):
        return self.session.post(self.base_url + url, **kwargs)