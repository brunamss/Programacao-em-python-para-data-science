VENDAS = {
'SETOR1':{
'MÊS 1':[150,200,300]},
'SETOR2':{
'MÊS 2':[300,250,300]},
'SETOR3':{
'MÊS 3':[15,20,300]},
'SETOR4':{
'MÊS 4':[150,2000,300000],
}
}



# Você foi contratado para verificar qual setor vendeu mais



setor_1 = sum( VENDAS['SETOR1']['MÊS 1'])
setor_2 =  sum(VENDAS['SETOR2']['MÊS 2'])
setor_3 =  sum(VENDAS['SETOR3']['MÊS 3'])
setor_4 =  sum(VENDAS['SETOR4']['MÊS 4'])


setores =  ['setor 1', 'setor 2', 'setor 3', 'setor 4']


todas_vendas = []
todas_vendas += (setor_1, setor_2,setor_3, setor_4)
maior_venda =  max(todas_vendas)
setor_q_mais_vendeu = todas_vendas.index(maior_venda)
print('O SETOR QUE MAIS VENDEU - ', setores[setor_q_mais_vendeu])




# qual a media total de vendas?
soma  =  sum(todas_vendas)/len(todas_vendas)
print('R$ total ', soma)


# Qual a maior venda?
print(maior_venda)


# Utilize as estruturas que você já conhece.