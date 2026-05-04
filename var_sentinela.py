# Exemplo de Uso da Variavel Sentinela True:
while True:
  comando = input("digite um comando-para parar digite'sair'")
  if comando == "sair":
    break
print(F"Executando:{comando}")