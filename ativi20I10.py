#crie ujma funcao que receba tres parametros:

#1. preco_original_percentual (percental de desconto)
#2.desconto_percentual (percentual de desconto, por exemplo: 10 para  10%)
#3.imposto_petrcentual (percentual)

#crie uma funcao para calcular o desconto e outra para calcular o imposto 
# A funcao calcular_preco_final deve retornar o preco final do produto , considerando os calculos abaixo
  
# - subtraia o desconto do preco original
# - adicione o imposto ao resultado anterior

# exemplo 
# - calcular_preco_final(100, 10, 5) ---> Resultado 94.5 (10% de desconto = 90,5% de imposto sobre 90 = 4.5 -->total 94.55).

# -requisitos:
# a funcao deve validar que parametros sejam numeros positivos. se algun valor for invalido retorne uma mensagem de erro
#(ex: "erro: parametro invalido");