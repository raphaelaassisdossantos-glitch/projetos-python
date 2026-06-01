# Aluno1:Padronizar nome do Filme 
def formatar(nome):
    return nome.upper()
#Aluno2 Verificador de Idade
def verificar_idade(idade):
    if idade >= 18:
        return "Autorizado"
    else:
        return "Não Autorizado"
#Aluno3 : Mensagem de retorno
def gerar_mensagem(status):
    if status == "Autorizado":
      return "Tenha uma otíma Sessão !"
    else:
        return "Sentimos, mas você não tem idade minima."
#Aluno4: Execução do Algoritmo
filme_entrada = input("Digite o filme Escolhido ")
idade_entrada = int(input("Digite a sua Idade "))
nome_final = formatar(filme_entrada)
status_acesso = verificar_idade(idade_entrada)
mensagem = gerar_mensagem(status_acesso)
print(F"\nfilme:{nome_final}")
print(F"Status:{status_acesso}")
print(F"Mensagem:{mensagem}")



