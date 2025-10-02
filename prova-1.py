#Maria Júlia Da Silva
#0220482523039
print("Maria Julia Da Silva, RA: 0220482523039 ")

preco_custo = float (input("Digite o Preço de custo do produto "))
preco_venda = float (input("Digite o Preço de venda do produto "))

lucro = preco_venda - preco_custo

margem = lucro / preco_custo * 100
if margem >= 30 :
    print("Margem Exelente! ")
elif margem >= 10 or margem >= 30 :
    print("Margem Satisfatória. ")
else:
    print("Margem Baixa: Avaliar preço de venda.")
