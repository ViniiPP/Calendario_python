import calendar

try: # É "TIPO UM WHILE" PORÉM DIFERENTE
    entrada = int(input("Digite um ano para o calendário: "))
    if (1 > entrada or entrada > 9999):  #CASO DO ERRO
        print("Escolha outro ano")
    else:                                #CASO DE CERTO
        for i in range(12):
            print(calendar.month(entrada, i+1))
            print("--------------------")
except:                                  #CASO NÃO DE ENTRADA EM ALGUM VALOR
    print("Você não escolheu um ano")
