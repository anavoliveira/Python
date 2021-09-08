import unittest
from unittest import TestCase
from src.leilao.dominio import Usuario, Leilao, Lance

class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui')
        self.yuri = Usuario('Yuri')
        self.lance_do_gui = Lance(self.gui, 150.00)
        self.lance_do_yuri = Lance(self.yuri, 100.00)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_menor_valor_de_um_lance_quando_adicionado_em_ordem_crescente(self):
        
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100 
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_apenas_um_lance(self):
        
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_tres_lances(self):
        
        ana = Usuario('ana')
        lance_da_ana = Lance(ana, 200)
        
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_da_ana)
        self.leilao.propoe(self.lance_do_yuri)


        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(200.0, self.leilao.maior_lance)

    # se o leilão não tiver lances, deve permitir propor um lance
    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebidos)
    
    
    # se o ultimo usuario for diferente, deve permitir propor um lnace
    def teste_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        ana = Usuario('Ana')
        lance_da_ana = Lance(ana, 100)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_da_ana)
        
        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)

    # se o ultimo usuario for o mesmo, não deve permitir fazer um lance
    def teste_nao_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_igual(self):
        ana = Usuario('Ana')
        lance_1_da_ana = Lance(ana, 100)
        lance_2_da_ana = Lance(ana, 200)

        with self.assertRaises(ValueError):
            self.leilao.propoe(lance_1_da_ana)
            self.leilao.propoe(lance_2_da_ana)
        
    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        
        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(self.lance_do_yuri)
 
 

if ( __name__ == "__main__"):
    unittest.main()