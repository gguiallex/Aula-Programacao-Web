# Programação Web - Atividades em Django

Este repositório contém as atividades desenvolvidas na disciplina de Programação Web (UFLA), utilizando o framework Django.  
O desenvolvimento está sendo feito de forma incremental, com cada etapa representando uma evolução do projeto conforme as orientações do professor.

## Organização das Pastas

- **aula-django-01**: Primeira etapa da atividade.
- **aula-django-02**: Segunda etapa, contendo tudo da etapa 1 **mais** os novos requisitos pedidos.
- **aula-django-03**: Terceira etapa, contendo tudo da etapa 2 **mais** as novas funcionalidades solicitadas, e assim por diante.

Cada pasta contém o código correspondente à etapa, facilitando o acompanhamento da evolução do projeto.

## Como rodar cada etapa

1. Entre na pasta da etapa desejada:
   ```
   cd aula-django-0X/code
   ```
2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   .\venv\Scripts\Activate
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
   *(Se não houver um arquivo requirements.txt, instale o Django manualmente: `pip install django`)*

4. Rode as migrações e o servidor:
   ```
   python manage.py migrate
   python manage.py runserver
   ```

## Observações

- Este repositório é para fins de estudo e acompanhamento das atividades propostas pelo professor.
- O código de cada etapa pode ser diferente, pois reflete o progresso incremental das tarefas.
- Sempre consulte o README de cada pasta (se houver) para instruções específicas daquela etapa.

## Créditos

Atividade baseada nas orientações do professor Jesimar da disciplina de Programação Web - UFLA.

---
