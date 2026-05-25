#Multiplas Funçoes -- Exercicio Controle de Qualidade --
def cabecalho():
    print("\n" + "=" * 30)
    print("SISTEMA DE QUALIDADE")
def verificador_status(peso):
    if peso >= 50 and peso <=100:
       return "Aprovada"
    else:
       return "Reprovado"
cabecalho()
peso_item = float(input("Digite o Peso do Item em Gramas: "))
status = verificador_status(peso_item)
print(F"resultado da Inspeção:{status}")
print("=" * 30)