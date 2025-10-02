#Maria Júlia Da Silva
#0220482523039
print("Maria Julia Da Silva, RA: 0220482523039 ")

peso = float(input("Qual o peso da encomenda? "))
distancia = float(input("Qual a distância da entrega em km? "))

custo_base = (peso * 1.5) + (distancia * 0.25)
if custo_base >= 200 : 
    desconto = custo_base - (custo_base * 0.10)
    print("Seu valor original é: " , custo_base , "E com desconto ficou: " , desconto)
elif custo_base >= 50 or custo_base >= 200:
    print("Seu valor final não se aplica desconto: " , custo_base )
else:
    taxa = custo_base + 5
    print("Seu valor original é: " , custo_base , "E com custo de manuseio ficou: " , taxa)