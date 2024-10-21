import requests
import json

def consulta_cnpj(cnpj):

    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request("GET", url, params=querystring)

    resp = json.loads(response.text)

    print(resp)
    return resp['nome'], resp['fantasia'],resp['abertura'],resp['natureza_juridica'],resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro'], resp['municipio'], resp['uf'], resp['cep'],  resp['email'],resp['telefone']






if __name__=='__main__':
    c = consulta_cnpj(41794502000119)
    print(c)
    pass