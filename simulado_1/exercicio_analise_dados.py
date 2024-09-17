# Exercicio para alunos de administracao e economia
# Evento Gastronomico realizado na faculdade para arrecadar fundos para uma entidade filantrópica
#Lista dos organizadores do evento
list_organizadores = ['bento', 'mariana', 'saulo']
# Fornecedores do evento
dict_fornecedor = {
    0: {'nome': 'Pastel Frito', 'vendas': 3000},
    1: {'nome': 'Massa da Mama', 'venda': 5000},
    2: {'nome': 'Pizza do Tio', 'vendas': 10000},
    3: {'nome': 'Rodizio Mineiro', 'vendas': 3900},
}
# Clientes que consumiram no evento
list_cliente = ['rafael','douglas','amanda','jorge','jeffri','carol','cristian','leonardo','maria','luana','vanessa','jose','maria','bento','mariana','saulo','glauco','ze','maria','bola']
# Despesas do evento
locacao = 0.10
limpeza = 700
seguranca = 800
outras_despesas = 500

#1 Calcule o total de vendas usando o for loop no dict
total_vendas = 0
for fornecedor in dict_fornecedor.values():
    total_vendas += fornecedor.get('vendas', fornecedor.get('venda', 0))
print(total_vendas)

#Os professores doaram 5000,00, cada professor doou 1000,00
#2 Crie um dicionário com o nome e valor
doacao_professor = {"Alice": "1000,00",
                    "Ronaldo": "1000,00",
                    "Fernando": "1000,00",
                    "Wesley": "1000,00",
                    "Daniela": "1000,00"}

#3 Criar uma lista com o nome dos professores
lista_professores = ["Alice", "Ronaldo", "Fernando", "Wesley", "Daniela"]

#4 Adicionar essa lista dos professores na lista de clientes
nova_lista = list_cliente + lista_professores
print(nova_lista)

#5 Calcular quantas pessoas estiveram e a medida de gasto por pessoa
total_pessoas = len(list_cliente) + len(lista_professores)
total_vendas = 21900
media_gasto = total_vendas/total_pessoas
print(f"Total de pessoas: {total_pessoas}")
print(f"Média de gasto por pessoa: R$ {media_gasto:.2f}")

#6 Encontrar quem foi o 10 consumidor e retire da lista
decimo_consumidor = nova_lista[9]
nova_lista.pop(9)
print(f"10º consumidor: {decimo_consumidor}")
print(f"Lista após remover o 10º consumidor: {nova_lista}")

#7 Encontre o nome "bola" inserido incorretamente na lista e retire da lista
if 'bola' in list_cliente:
  list_cliente.remove('bola')
  print("o nome 'bola' foi removido")
else:
  print("não foi achado o nome 'bola'")

#8 Verificar se todos os organizadores estão na lista
for nome in list_organizadores:
  if nome in list_cliente:
    print(f"{nome} esta na lista")
  else:
    print(f"{nome} nao esta na lista")

#9 Tira-los da lista
nova_lista.pop(12)
nova_lista.pop(12)
nova_lista.pop(12)
print(f"a nova lista sem os organizadores é: {nova_lista}")

#10 Fazer uma função que calcule o lucro líquido do evento
custo_locacao = total_vendas *locacao
total_custo = custo_locacao + limpeza + seguranca + outras_despesas
def calc_lucro_liquido(vendas, despesas):
  lucro = vendas - despesas
  return lucro
lucro_liquido = calc_lucro_liquido(total_vendas, total_custo)
print(f"lucro liquido do evento foi de {lucro_liquido}")
