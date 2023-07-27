from time import sleep

saldo = 0
tot_saque = 0
limite = 500
extrato = ""
print('{:=^29}'.format(' BANCO SBAN '))

nome = str(input("Informe seu nome: ").strip().upper())
print()
print(f"Olá, {nome}!")


while True:
    print("Escolha uma das opções abaixo: ")
    print("=============================")
    print('[1] Depositar \n[2] Sacar \n[3] Extrato \n[4] Sair')
    print("=============================")

    opcao = int(input('Informe a opção escolhida: '))
    if opcao == 1:
        while True:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito de R${valor:.2f}\n"
                break
            print("Valor inválido.")
        print(f"Depósito de R${valor :.2f} realizado com sucesso!")

    elif opcao == 2:
        if tot_saque >= 3:
            print("Saque não realizado. Total de saques excedidos por mês.")
        else:
            saque = float(input("Informe o valor do saque: "))
            if saque > saldo:
                print("Saque não realizado.Saldo insuficiente!")
            elif saque < 0:
                print("Valor inválido!")
            elif saque > 500:
                print("Valor diário de saque excedido!")
            else:
                tot_saque += 1
                saldo -= saque
                print("Aguarde contagem de notas...")
                sleep(2)
                print(f"SAQUE REALIZADO COM SUCESSO!.\nSALDO ATUAL: R${saldo:.2f}")
                extrato += f"Saque de R${saque:.2f}\n"
    elif opcao == 3:
        print('{:=^40}'.format(' EXTRATO '))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual R${saldo:.2f}")
        print('{:=^40}'.format(' FIM DO EXTRATO '))
    elif opcao ==4:
        print('SAINDO...\nO BANCO SBAN AGRADECE A VISITA!')
        break
    else:
        print("Operação inválida!")












