#Maria Júlia Da Silva
#0220482523039
print("Maria Julia Da Silva, RA: 0220482523039 ")

pureza = float(input("Digite a pureza do lote: "))
massa_total = float(input("Digite a massa total do lote: "))
taxa_contaminacao = float(input("Digite a taxa de contaminação: "))

FD = (pureza * 100) - (taxa_contaminacao * 50)

if massa_total > 1000:
    P_base = 10.00
else:
    P_base = 12.50

if FD > 90 and pureza > 0.98:
    classificacao = "Premium (Venda Imediata)"
    P_final_kg = P_base * 1.50
elif 70 <= FD <= 90 and taxa_contaminacao < 0.05:
    classificacao = "Padrão (Venda Normal)"
    P_final_kg = P_base * 1.10
elif FD < 70 or pureza < 0.90:
    classificacao = "Reprovado (Descarte ou Re-processamento)"
    P_final_kg = P_base * 0.25
else:
    classificacao = "Aceitável (Margem Mínima)"
    P_final_kg = P_base * 0.90

Preco_Total_Final = P_final_kg * massa_total

print("--- Resultado da Avaliação ---")
print(f"Fator de Desempenho (FD): {FD:.2f}")
print(f"Preço Base por kg: R$ {P_base:.2f}")
print(f"Classificação: {classificacao}")
print(f"Preço Final por kg: R$ {P_final_kg:.2f}")
print(f"Preço Total Final do Lote: R$ {Preco_Total_Final:.2f}")
