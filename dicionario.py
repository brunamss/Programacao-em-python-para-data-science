loja = {

    'produtos':{

    'eletronicos' : {'hd': 500, 'fone': 200},
    'cama, mesa e banho': {'lençol': 150, 'toalhas': 150},
    'sapatos': {'nike': 1500, 'adidas':550}

    },
    'assinaturas':{

    'netflix': 20.99,
    'globo.com': 50.00

    }


}

menu_sessao = input ('Digite o que deseja: ')
prod = input ('Digite seu produto: ')
item = input ('Digite seu item: ')

print (loja [menu_sessao][prod][item])