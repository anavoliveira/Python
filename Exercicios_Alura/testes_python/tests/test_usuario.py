import pytest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__))))

from src.leilao.dominio import Usuario, Leilao, Lance
from src.leilao.excecoes import LanceInvalido

@pytest.fixture
def ana():
    return Usuario('Ana',100)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(ana, leilao):
    ana.propoe_lance(leilao, 50.0)

    assert ana.carteira == 50.0

def test_deve_permitir_propor_lance_quando_valor_for_menor_que_o_valor_da_carteira(ana, leilao):
    ana.propoe_lance(leilao, 50.0)

    assert ana.carteira == 50.0
    
def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(ana, leilao):
    ana.propoe_lance(leilao, 100.0)

    assert ana.carteira == 0.0

def test_nao_devee_permitir_propor_lance_com_valor_maior_que_o_da_carteira(ana, leilao):
    with pytest.raises(LanceInvalido):
        ana.propoe_lance(leilao, 101.0)

        assert ana.carteira == 100.0

