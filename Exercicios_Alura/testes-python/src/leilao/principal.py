from  dominio import Usuario, Lance, Leilao

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_gui = Lance(gui, 150.00)
lance_do_yuri = Lance(yuri, 100.00)
 

leilao = Leilao('Celular')

leilao.propoe(lance_do_gui)
leilao.propoe(lance_do_yuri)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')


print(f'O menor lance foi de {leilao.menor_lance} e o maior valor foi de {leilao.maior_lance}')