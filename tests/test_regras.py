import pytest
from regras import pedido_atingiu_valor_minimo


def test_pedido_atinge_valor_minimo_no_limite():
    
    resultado = pedido_atingiu_valor_minimo(30)
    assert resultado is True


def test_pedido_abaixo_do_valor_minimo():
    
    resultado = pedido_atingiu_valor_minimo(29.90)
    assert resultado is False


def test_pedido_com_valor_negativo_gera_erro():
   
    with pytest.raises(ValueError, match="O valor do pedido não pode ser negativo."):
        pedido_atingiu_valor_minimo(-10)