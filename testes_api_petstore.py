import pytest
import requests

url = 'https://petstore.swagger.io/v2/user'

def testar_incluir_usuario():
    #Configura
    status_code_esperado = 200          # Comunicação
    codigo_esperado = 200               # Funcional
    tipo_esperado = 'unknown'           # Fixo como desconhecido
    mensagem_esperada = '19779'         # ID do usuário

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.post(url,
                             data=open('json/usuario1.json', 'rb'),
                             headers=headers)
    corpo_da_resposta = resposta.json()
    print(resposta)                     # Status Code
    print(resposta.status_code)         # Status Code
    print(corpo_da_resposta)            # Response Body / Corpo da resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_consultar_usuario():
    # Configura
    username = 'karladaiany'            # input / entrada para consulta
    id_esperado = 19779
    username_esperado = 'karladaiany'
    email_esperado = 'karladaiany@hotmail.com'
    telefone_esperado = '45999999779'
    user_status_esperado = 0
    status_code_esperado = 200          # comunicação

    headers = {'Content-Type': 'application/json'}

    #Executa
    resposta = requests.get(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)                     # Status Code
    print(resposta.status_code)         # Status Code
    print(corpo_da_resposta)            # Response Body / Corpo da resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado

def testar_alterar_usuario():
    # Configura
    username = 'karladaiany'
    status_code_esperado = 200          # Comunicação
    codigo_esperado = 200               # Funcional
    tipo_esperado = 'unknown'           # Fixo como desconhecido
    mensagem_esperada = '19779'         # ID do usuário

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.put(url=f'{url}/{username}',
                             data=open('json/usuario2.json', 'rb'),
                             headers=headers)
    corpo_da_resposta = resposta.json()
    print(resposta)                     # Status Code
    print(resposta.status_code)         # Status Code
    print(corpo_da_resposta)            # Response Body / Corpo da resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_excluir_usuario():
    # Configura
    username = 'karladaiany'            # input / entrada para exclusão e retorno na resposta (message)
    status_code_esperado = 200          # Comunicação
    tipo_esperado = 'unknown'           # Fixo como desconhecido

    headers = {'Content-Type': 'application/json'}

    #Executa
    resposta = requests.delete(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)                     # Status Code
    print(resposta.status_code)         # Status Code
    print(corpo_da_resposta)            # Response Body / Corpo da resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == status_code_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == username

def testar_consultar_usuario_e_extrair_senha(username):
    # Configura
    id_esperado = 19779
    username_esperado = 'karladaiany'
    email_esperado = 'karladaiany@hotmail.com'
    telefone_esperado = '45999999779'
    user_status_esperado = 0
    status_code_esperado = 200          # comunicação

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)                     # Status Code
    print(resposta.status_code)         # Status Code
    print(corpo_da_resposta)            # Response Body / Corpo da resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado

    return corpo_da_resposta['password']

def testar_login(username, password):
    # Configura
    status_code_esperado = 200          # Comunicação / Funcional
    tipo_esperado = 'unknown'           # Fixo como desconhecido
    mensagem_esperada = 'logged in user session'    # Começo da mensagem

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/login?username={username}&password={password}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)                     # Status Code
    print(resposta.status_code)         # Status Code
    print(corpo_da_resposta)            # Response Body / Corpo da resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == status_code_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert mensagem_esperada in corpo_da_resposta['message']

    #token = corpo_da_resposta['message']
    #print(f'{token[22:13]}')
    #return token[22:13]

    token = corpo_da_resposta['message'].rpartition(':')[-1]
    print(f'token: {token}')
    return token

def testar_orquestracao_consultar_senha_e_realizar_login():
    # Vai orquestrar as chamadas de duas funções para atingir o seu objetivo

    # Configura
    username = 'karladaiany'

    # Executa
    password = testar_consultar_usuario_e_extrair_senha(username)
    token = testar_login(username, password)