# Bookstore
# Bookstore API

API desenvolvida com Django REST Framework.

## Deploy

O projeto originalmente foi preparado para deploy no Heroku conforme a proposta do módulo. Como o Heroku deixou de oferecer o mesmo modelo gratuito utilizado na aula, o deploy foi adaptado para o PythonAnywhere.

A aplicação está publicada em:

https://silas34.pythonanywhere.com/

Endpoint de produtos:

https://silas34.pythonanywhere.com/products/

## Integração contínua e deploy

O projeto utiliza GitHub Actions para automatizar o processo a cada push na branch `main`.

O workflow localizado em:

`.github/workflows/build.yml`

executa:

1. Checkout do código.
2. Configuração do Python 3.13.
3. Instalação do Poetry.
4. Instalação das dependências.
5. Execução dos testes automatizados.
6. Deploy/reload da aplicação no PythonAnywhere quando os testes são aprovados.

O token de acesso do PythonAnywhere é armazenado com segurança nos Secrets do GitHub Actions através da variável:

`PYTHONANYWHERE_API_TOKEN`

## Testes

Os testes automatizados são executados pelo GitHub Actions antes do deploy.

Atualmente o projeto possui 12 testes, todos passando com sucesso.

## Banco de dados

O banco SQLite local não é versionado. O arquivo `db.sqlite3` está incluído no `.gitignore`.

As migrations são executadas no ambiente do PythonAnywhere.
