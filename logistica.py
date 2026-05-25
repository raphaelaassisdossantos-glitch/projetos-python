#Calculadora de Frete --
def cabecalho():
    print("\n" + "=" * 30)
    print('SISTEMA DE LOGISTICA')
def calcular_frete(peso_carga):
    if peso <= 20 and  peso >20:
        return 10.00
    else:
        return 15.00
cabecalho()
peso_carga = float(input("Digite o Peso da Carga em (kg):"))
frete = calcular_frete(peso_carga)
print(F"O valor do frete é: R$ {frete:.2f}")
print("=" * 30)
