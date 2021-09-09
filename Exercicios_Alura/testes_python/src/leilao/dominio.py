

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__))))

from src.leilao.excecoes import LanceInvalido

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        
        if valor> self.__carteira:
            raise LanceInvalido("Nao pode propor lance maior que o valor da carteira")
        
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor
  
    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao 
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            
            if not self._tem_lances():
                self.menor_lance = lance.valor
            
            self.maior_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise LanceInvalido('Erro ao propor o lance')

    @property
    def lances(self):
        return self.__lances[:]
    
    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuario nao pode dar dois lances seguidos")
    
    def _valor_maior_que_o_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O valor do lance precisa ser maior que o anterior")
    
    def _lance_eh_valido(self, lance):
        return not self.__lances or (self._usuarios_diferentes(lance) and self._valor_maior_que_o_anterior(lance))
