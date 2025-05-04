Challenger-1-Furia

Repositório desenvolvido como parte do processo seletivo para a posição de Assistente de Engenharia de Software na organização FURIA.
Este projeto tem como finalidade demonstrar minhas habilidades e conhecimentos para exercer o cargo.  
As soluções aqui apresentadas visam refletir minhas ideias e meus conhecimentos atuais. 

Linguagens Utilizadas:
HTML5 
CSS 
Python - Django (Web Development)

📁 Estrutura do Projeto
Ele se encontra na Master Branch. Abaixo, segue o passo a passo para executa-lo localmente. 

Challenger-1-Furia/
├── challenger_furia/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── staticfiles/
│   └── admin/
├── db.sqlite3
└── manage.py

Descrição dos componentes:

* **challenger\_furia/**: Estrutura Principal com todos arquivos.

  * `__init__.py`: Indica que este diretório é um pacote Python.
  * `asgi.py`: Configuração para a interface ASGI, usada para deploys assíncronos.
  * `settings.py`: Arquivo de configurações do projeto.
  * `urls.py`: Define as rotas principais do projeto.
  * `wsgi.py`: Configuração para a interface WSGI, usada para deploys síncronos.

* **core/**: Aplicação principal do projeto.

  * `__init__.py`: Indica que este diretório é um pacote Python.
  * `admin.py`: Configurações para o painel administrativo do Django.
  * `apps.py`: Configurações da aplicação.
  * `migrations/`: Diretório que armazena os arquivos de migração do banco de dados.

    * `__init__.py`: Indica que este diretório é um pacote Python.
  * `models.py`: Definição dos modelos de dados.
  * `tests.py`: Testes automatizados da aplicação.
  * `views.py`: Lógica das views da aplicação.

* **staticfiles/**: Diretório para arquivos estáticos (CSS, JavaScript, imagens).

  * `admin/`: Arquivos estáticos relacionados ao painel administrativo do Django.

* **db.sqlite3**: Banco de dados SQLite utilizado pelo projeto.

* **manage.py**: Script de gerenciamento do Django, utilizado para executar comandos administrativos.

🚀 Como Executar!!

    Clone o repositório:

git clone https://github.com/Marcus8843/Challenger-1-Furia.git

Navegue até o diretório do projeto:

cd Challenger-1-Furia

Instale as dependências:

No caso, como é um projeto Django, primeiramente precisa escolher se rodará em um ambiente virtual.
Eu utilizo o venv. 

`python3 venv venv`

Após isso, execute o ambiente virtual:
LINUX:
`source venv/bin/activate`
MAC/WINDOWS
`venv\Scripts\activate`

Comandos Necesssários para executar posteriormente:

`pip install django`
`python manage.py migrate`
`python manage.py createsuperuser` Caso queira executar comandos e editar o arquivo.

Comando Principal:
`python manage.py runserver`

No próprio terminal irá conter o link para a porta local: http://127.0.0.1:8000. 


📄 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

📬 Contato

Para dúvidas ou sugestões, entre em contato:

    Nome: Marcus Vinicius

    Email: marcusvinicius8843@gmail.com     \   Telefone: 62 999835678

    LinkedIn: https://www.linkedin.com/in/marcus-vinicius-799686209/
