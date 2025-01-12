import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_url_shortner_success(client):
    data = {"original_url": "https//:exemplo.com/url-longa"}
    response = client.post("/shortner", json=data)
    assert response.status_code == 201
    assert "short_url" in response.json



# falha - url original inválida
# falha - url original que já foi encurtada antes
# falha - dados faltando na requisição
# falha - url original muito longa
# falha - url gerada já existe
# sucesso - verifica se retorna a url encurtada
# verificar tempo de resposta
# verifica redirecionamento após um tempo - se ainda funciona
