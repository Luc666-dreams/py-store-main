import json, os

#Abrir o arquivo headers.json é obter as informações pro modulo.
with open(os.path.join(os.path.dirname(__file__), "json", 'headers.json'), encoding="utf8") as b:
    headers = json.load(b)

#Abrir o arquivo headers.json é obter as informações pro modulo.
with open(os.path.join(os.path.dirname(__file__), "json", 'data.json'), encoding="utf8") as c:
    info = json.load(c)


