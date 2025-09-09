import requests
import json
import random
import string
#####
# Desafio API - Parte 1 - TC01

#TC01.001 - Criar um usuário (https://demoqa.com/Account/v1/User)
#TC01.002 - Gerar um token de acesso (https://demoqa.com/Account/v1/GenerateToken)
#TC01.003 - Confirmar se o usuário criado está autorizado (https://demoqa.com/Account/v1/Authorized)
#TC01.004 - Listar os livros disponíveis (https://demoqa.com/BookStore/v1/Books)
#TC01.005 - Alugar dois livros de livre escolha (https://demoqa.com/BookStore/v1/Books)
#TC01.006 - Listar os detalhes do usuário com os livros escolhidos (https://demoqa.com/Account/v1/User/{userID})
#####

base_url = "https://demoqa.com"

def print_response(response):
    """Imprime a resposta em JSON."""
    try:
        print(f"Response Body: {json.dumps(response.json(), indent=2)}")
    except json.JSONDecodeError:
        # Se não for JSON, imprime como texto simples
        print(f"Response Body: {response.text}")

def run_api():
    # Gerando um username e password únicos para evitar conflitos

    username = f"user{random.randint(1000,9999)}"
    password = f"Password@{random.randint(1000,9999)}"

    headers = {
        "Content-Type": "application/json"
    }

    #TC01.001 - Criar um usuário
    print("TC01.001 - Criar um usuário")
    create_user_payload = {
        "userName": username,
        "password": password
    }
    create_user_response = requests.post(
        f"{base_url}/Account/v1/User",
        headers=headers,
        data=json.dumps(create_user_payload)
    )
    
    if create_user_response.status_code == 201:
        user_id = create_user_response.json().get("userID")
        print(f"Sucesso! Usuário criado com UserID: {user_id}\n")
        
    else:
        print("Falha ao criar usuário.")
        return False

    #TC01.002 - Gerar um token de acesso
    print("TC01.002 - Gerar um token de acesso")
    generate_token_payload = {
        "userName": username,
        "password": password
    }
    generate_token_response = requests.post(
        f"{base_url}/Account/v1/GenerateToken",
        headers=headers,
        data=json.dumps(generate_token_payload)
    )

    if generate_token_response.status_code == 200:
        token = generate_token_response.json().get("token")
        print("Sucesso! Token gerado.\n")
    else:
        print("Falha ao gerar token.")
        return False

    # Preparar headers com o token para as próximas requisições
    auth_headers = headers.copy()
    auth_headers["Authorization"] = f"Bearer {token}"

    # TC01.003 - Confirmar se o usuário criado está autorizado
    print("TC01.003 - Confirmar se o usuário criado está autorizado")

    authorized_response = requests.post(
        f"{base_url}/Account/v1/Authorized",
        headers=auth_headers,
        data=json.dumps(generate_token_payload)
    )
    print_response(authorized_response)

    if authorized_response.status_code != 200 or not authorized_response.json():
        print("Usuário não autorizado.")
        return False
    else:
        print("Sucesso! Usuário está autorizado.\n")

    # TC01.004 - Listar os livros disponíveis
    print("TC01.004 - Listar os livros disponíveis")
    list_books_response = requests.get(f"{base_url}/BookStore/v1/Books", headers=auth_headers)
    print_response(list_books_response)

    if list_books_response.status_code != 200:
        print("Falha ao listar livros")
        return False

    all_books = list_books_response.json().get("books", [])
    if len(all_books) < 2:
        print("Não há livros suficientes para alugar.")
        return False
    else:
        print(f"Sucesso! {len(all_books)} livros encontrados.\n")

    #TC01.005 - Alugar dois livros de livre escolha
    print("TC01.005 - Alugar dois livros de livre escolha")

    books_to_add = [all_books[0], all_books[1]]
    isbn1 = books_to_add[0]['isbn']
    isbn2 = books_to_add[1]['isbn']
    print(f"Livros selecionados para aluguel (ISBN): {isbn1} e {isbn2}")

    add_books_payload = {
        "userId": user_id,
        "collectionOfIsbns": [
            {"isbn": isbn1},
            {"isbn": isbn2}
        ]
    }
    add_books_response = requests.post(
        f"{base_url}/BookStore/v1/Books",
        headers=auth_headers,
        data=json.dumps(add_books_payload)
    )
    print_response(add_books_response)

    if add_books_response.status_code != 201:
        print("Falha ao alugar os livros.")
        return False
    else:
        print("Sucesso! Livros alugados.")

    # TC01.006 - Listar os detalhes do usuário com os livros escolhidos
    print("TC01.006 - Listar os detalhes do usuário com os livros escolhidos")
    get_user_response = requests.get(
        f"{base_url}/Account/v1/User/{user_id}",
        headers=auth_headers
    )
    print_response(get_user_response)

    if get_user_response.status_code == 200:
        user_books = get_user_response.json().get("books", [])
        if len(user_books) == 2:
            print("Sucesso! Usuário possui os dois livros alugados.")
            return True
    else:
        print("Erro! Não foi possível obter os detalhes do usuário.")
        return False

if __name__ == "__main__":
    run_api()