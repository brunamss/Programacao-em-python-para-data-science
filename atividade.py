






# MINHA PARTE



pe =  input('Deseja acessar o banco? ')


while pe  == 'sim':
    senha  =  input('Senha: ')
    if senha  == '123':
        print('banco X')
        print('''Menu:
            
            1 - saque
            2 - deposito
            3 - extrato
            4 -  sair 
            
            
            
            ''')
        saldo = 1000
        saque = 0  
        deposito = 0
        op =  input('escolha a operação: ')
        if  op == '1':
            
            saque = float (input ('saque: '))
            saldo =saldo - saque
            x = saldo
            print (saldo)

        if op == '2':
            
            deposito = float (input('deposito: '))
            saldo =x + deposito
            y = saldo
            print (saldo)

        if op == '3':
           
            extrato = [saldo, x, y]

            # extrato.append(saque)
            # extrato.append(deposito)
            print(extrato)



            pe =  input('Deseja acessar o banco? ')

        if op  == '4':
            print ('Obrigado pelo seu acesso')
            exit()


            
            pass
    else:
        print('não te encontramos no nosso banco')        
            




# PARTE DA PROFESSORA


