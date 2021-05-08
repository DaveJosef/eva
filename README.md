# EvA

Aplicação web para o controle de eventos acadêmicos  

**Preparação**

Criar ambiente virtual:  

```
python3 -m venv venv
```

Entrar no ambiente virtual:  

```
source venv/bin/activate
```

**Depedências**

Instalar as dependências:  

```
pipenv install
```

**Banco de Dados**

Criar super-usuário:

```
python3 manage.py createsuperuser
```

Criar models da aplicação:

```
python3 manage.py makemigrations
```

Executar ações pendentes do banco:

```
python3 manage.py migrate
```

**Execução**

Rodar aplicação:  

```
python3 manage.py runserver
```
