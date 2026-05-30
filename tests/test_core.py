from src.core import processar_pagamento

def test_processar_pagamento_sucesso():
    assert processar_pagamento(100) == "Sucesso"

def test_processar_pagamento_erro():
    assert processar_pagamento(-5) == "Erro: Valor inválido"