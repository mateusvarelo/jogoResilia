
def mensagem_abertura(opcao):
    print("*"*50)
    print("***Inicio de jogo!***")
    print("\n´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶/n"
        "\n´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´¶¶"
        "\n´´´´´´¶¶¶¶¶´´´´´´´¶¶´´´´´´´´´´´´´´¶¶"
        "\n´´´´´¶´´´´´¶´´´´¶¶´´´´´¶¶´´´´¶¶´´´´´¶¶"
        "\n´´´´´¶´´´´´¶´´´¶¶´´´´´´¶¶´´´´¶¶´´´´´´´¶¶"
        "\n´´´´´¶´´´´¶´´¶¶´´´´´´´´¶¶´´´´¶¶´´´´´´´´¶¶"
        "\n´´´´´´¶´´´¶´´´¶´´´´´´´´´´´´´´´´´´´´´´´´´¶¶"
        "\n´´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´¶¶"
        "\n´´´¶´´´´´´´´´´´´¶´¶¶´´´´´´´´´´´´´¶¶´´´´´¶¶"
        "\n´´¶¶´´´´´´´´´´´´¶´´¶¶´´´´´´´´´´´´¶¶´´´´´¶¶"          "\n´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶´´´´¶¶´´´´´´´´¶¶´´´´´´´¶¶"
        "\n´¶´´´´´´´´´´´´´´´¶´´´´´¶¶¶¶¶¶¶´´´´´´´´´¶¶"
        "\n´¶¶´´´´´´´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´¶¶"
        "\n´´¶´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´¶¶"
        "\n´´¶¶´´´´´´´´´´´¶´´¶¶´´´´´´´´´´´´´´´´¶¶"
        "\n´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´¶¶"
       "\n´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶")
    print("*"*50)
    print("Vamos jogar?Sim ou Não?")
    print("Para sair do jogo tecle quarquer letra!")
    opcao = input(": ")
    return opcao.lower()

def primeirocenario():
    print(
        "\nEm uma noite de domingo em uma cidade grande um homem e que vinha de" 
        "\nmoto atravessando um túnel  onde á fortemente a presença de comunidades" 
        "\ndo crime, e surpreendido com um assaltante, sua moto tinha sido"
        "\ncomprada recentemente.Ele está muito nervoso, sem saber o que fazer."
         )
def segundocenario():
    print(
          "Ao chegar em casa o homem descansa e conversa com amigo, casa dele um"
          "pouco bagunçada, então ele pensa em situações que pode levar ao destino" 
          "que a moto está!Escolha a melhor opção diante do que ele argumenta"
          )         
def informacoes(nome):
    print(
          "Diante dessa situação você vai tentar ajuda-lo! " 
          f"{nome} quais dessas situações indicaria:"
         )         

def fim_de_jogo():
   print("FIM")   
   print(
        "\n─────────────███████████████────────────"
        "\n──────────████▒▒▒▒▒▒▒▒▒▒▒▒▒████─────────"
        "\n────────███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███───────"
        "\n───────██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███─────"
        "\n──────██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒███████▒▒▒██────"
        "\n─────██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒██▒▒▒██───"
        "\n────██▒▒██▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒██──"
        "\n───██▒▒▒▒▒████▒▒▒▒██▒▒▒██▒▒▒▒▒▒▒▒██▒▒█──"
        "\n───█▒▒▒▒▒▒▒▒▒▒▒███░█▒▒▒█░███▒▒▒▒▒▒▒▒▒█──"
        "\n───█▒▒▒▒▒██████░░░░█▒▒▒█░░░░██████▒▒▒█──"
        "\n───█▒▒▒▒▒▒▒█░░░░▓▓██▒▒▒██▓▓░░░░█▒▒▒▒▒█──"
        "\n───█▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒██████▒█▒▒▒▒█──"
        "\n───█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒█──"
        "\n───█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░█▒▒▒█──"
        "\n───██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░█▒▒██──"
        "\n────██▒▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒██▒▒██───"
        "\n─────██▒▒▒▒▒▒█████▒▒▒▒▒▒█████▒▒▒▒▒██────"
        "\n──────██▒▒▒███▒▒▒▒▒████▒▒▒▒▒███▒▒██─────"
        "\n───────███▒▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒▒▒▒▒▒██──────"
        "\n─────────███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███───────"
        "\n───────────█████▒▒▒▒▒▒▒▒▒██████─────────"
        "\n───────────────████████████─────────────"
        ) 


resposta = 0
opcao = "sim"
nome = ""
while opcao == "sim":
    opcao = mensagem_abertura(opcao)
    if opcao == "sim":
        primeirocenario()  
        print("-"*50)
        print(
              "Precisa de sua ajuda para encontrar  a sua moto. Informe seu" 
              "nome para iniciar"
              )
        nome = input(":")
        print("-"*50)   
        print("1-Você empresta  o celular para ele ligar para policia.")
        print("2-Leva ele até a delegacia e aciona a policia civil.")
        print("3-leva ele para casa e faz um boletim de ocorrência e relaxa um pouco.")
        resposta = input(":")
        
        if resposta == 1:
            print(f"Opção escolhida {resposta} infelismente não e uma boa escolha") 
            print("Alternativa errada!Fim de jogo!Tentar novamente?SIm ou Não?")
            opcao = input(":")    
            if opcao.lower() == "sim":
                continue
            elif opcao.lower() == "não":
                 fim_de_jogo()
                 break
            else:
                fim_de_jogo()
                break

        elif resposta == 2:
            print(
                  "Abrir uma ocorrencia na delegacia e perda de tempo, eles" 
                  "fazem pouco caso para essas situações"
                  )
            print(f"Opção escolhida {resposta} infelismente não e uma boa escolha") 
            print("Alternativa errada!Fim de jogo!Tentar novamente?SIm ou Não?")      
            opcao = input(":") 
        elif resposta == 3:
            print("Boa escolha!Resolver as coisas com a cabeça fria e uma boa!") 
            print("Próximo cenario")  
            print("-"*50)   
            segundocenario()
            print("-"*50)   



    elif opcao == "não":
         opcao = "sim"
         continue
    else:
         fim_de_jogo()  
         break          
  