
# print("Boa noite!{nome}")

# idade = 36
# nome = "cecilia"
# mensagem = "Bem vindo ao  curso de Python"


# print (idade)
# print (mensagem)

# print("quantos anos você tem?")

#função somar
# def somar(a, b):
#     resultado = a + b
#     return resultado

# print (somar(3,5))

# def cumprimentar(nome):
#     print(f"Olá, {nome}! Seja bem-vinda.")
# cumprimentar("Cecilia")    

#Função

# largura = 7
# altura = 4
# def calcular_area(largura,altura):
#     return largura*altura
# area=calcular_area(largura,altura)
# print("Area do retangulo:", area)

#condicional

# numero = 1
# if numero >10 : 
#     print("Valor maior que dez")
# else:
#     print("Valor dez ou menor")    

#elif

# temperatura = 40
# if temperatura >30:
#     print("Clima quente")
# elif temperatura >20:
#     print("Clima ameno")
# else: 
#     print("Clima frio")    

#Loop

# comando = ""
# while comando != "sair":
#     comando= input("Digite 'Sair' para encerrar:")
# print("Programa encerrado")  

#outro loop

# for i in range(15):
#     print(i)

# nome = "Cecilia"

# def cumprimentar (nome):
#     print(f"Olá,{nome}!")



#Controle de Gastos Mensais

'''def calcular_saldo(rendimento,despesas):
    return rendimento - despesas

def sugerir_poupanca (saldo):
    return saldo * 0.2

# Entrada de dados
try:
    rendimento = float(input("Digite seu rendimentomensal (em reais):"))
    if rendimento < 0:
        raise ValueError("O rendimento não pode ser negativo.")
    
    despesas = float(input("Digite o total de suas despesas mensais (em reais):"))
    if despesas < 0:
      raise ValueError("As despesas não podem  ser negativas.")

    tem_poupanca = input("Você tem um plano de poupanca? (sim /não): "). strip(). lower()
    if tem_poupanca not in["sim" , "não"]:
        raise ValueError ("Resposta inválida. Digite 'sim ou não.")
    
# processamento

    saldo = calcular_saldo (rendimento , despesas)
    print(f"/n Seu saldo mensal é:R$ {saldo : .2f}")

    if saldo < 0:
        print("Atenção ! Suas despesas estão maiores que seus rendimentos .")
    elif saldo > 0:
        if tem_poupanca=="sim":
            poupanca_sugerida = sugerir_poupanca (saldo)
            print(f"Recomendamos poupar R${ poupanca_sugerida:.2f} este mês.")
        else:
            print("Considere criar um plano de poupança para aproveitar seu saldo positivo.")
    else:
        print("Seu orçamento esta equilibrado , sem saldo restante para poupar.")
except ValueError as e:
    print(f"Erro na entrada de dados : {e}")'''

