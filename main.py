menu = """"
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True: 
    opcao = input(menu)

    if opcao == "d":
      valor = float(input("informe o valor: "))

      if valor > 0:
         saldo += valor
         extrato += f"deposito: R$ {valor:.2f}"
      else:
        print("Operação falhou")


      
    elif opcao == "s":
      valor = float(input("informe o valor do saque: "))

      excedeu_saldo = valor > saldo
      excedeu_limite = valor > limite
      excedeu_saques = numero_saques >=LIMITE_SAQUES

      if excedeu_saldo:
         print("Operação falhou, você não tem saldo o suficiente")
      elif excedeu_limite:
         print("operação falhou, valor do saque excedo o limite")   
      elif excedeu_saques:
         print("operação falhou, numero máximo de saques excedido")   
      elif valor > 0:
         saldo -= valor
         extrato += f"saque: R$ {valor:.2f}\n"
      else:
         print("operação falhou, valor informado é invalido")

      if valor !=0:
         print("saque realizado com sucesso")
         


    elif opcao == "e":
      print("\n ===============Extrato===========")
      print("não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("=========================")




    elif opcao == "q":
       break
    else:
       print("operação invalida, por favor selecione novamente")