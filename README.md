1. Crie o ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows / Git Bash

2. Instale as dependências:

pip install flask pytest pytest-flask

3. Crie o arquivo requirements.txt para salvar as dependências:

pip freeze > requirements.txt

4. Rodar os testes com relatório de cobertura de testes

pytest --cov=app --cov-report=term-missing
