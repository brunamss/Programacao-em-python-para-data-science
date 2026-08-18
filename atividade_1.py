




dados  = {}



print('Cadastre-se:  ')


login = input('Login: ')
senha  = input('Senha: ') 


dados['login'] = login
dados['senha'] = senha  


print('dados cadastrados>>>', dados)




login_cad = input('Login: ')
senha_cad  = input('Senha: ') 


if login_cad == login and senha_cad == senha:
    print('Seja bem vindo  ao sistema Z')
    produtos = ['a','b','c']
    valores = [10.55,20.0,30.0]
else:
    print('Digite os dados corretamente...')    

Loja ={
    
    'produtos':{

        'roupas' : {'camiseta': 30.00, 'calça': 149.99, 'jaqueta':120.00},
        'tenis' : {'nike': 779.99, 'adidas': 360.00, 'vans': 430.00}

    }


}


produto = input ('Digite seu produto: ')
item = input ('Digite seu item: ')

print (Loja [produto][item])