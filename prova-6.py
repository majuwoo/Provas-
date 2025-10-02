#Maria Júlia Da Silva
#0220482523039
print("Maria Julia Da Silva, RA: 0220482523039 ")

R_investimento = float(input("Digite o retorno do investimento (em decimal, ex: 0.08 para 8%): "))
R_livre = float(input("Digite a taxa livre de risco (em decimal, ex: 0.03 para 3%): "))
Sigma = float(input("Digite o desvio-padrão da volatilidade (em decimal, ex: 0.10 para 10%): "))

if Sigma == 0:
    print("Erro: O desvio-padrão (Sigma) não pode ser zero.")
    Sharp = None
else:
    Sharp = (R_investimento - R_livre) / Sigma

Spread = R_investimento - R_livre

if Sharp is None:
    classificacao = "Não foi possível calcular devido a Sigma = 0."
elif Sharp > 1.5 and Spread > 0.05:
    classificacao = "Investimento Excelente: Alta performance ajustada ao risco."
elif (0.5 <= Sharp <= 1.5) or (Spread > 0.02):
    classificacao = "Investimento Bom: Risco e retorno moderados."
elif Sharp < 0.5 and R_investimento > 0:
    classificacao = "Investimento Aceitável: Retorno positivo, mas risco alto para o ganho."
else:
    classificacao = "Investimento Ruim: Não recomendado."

print("--- Resultados ---")
if Sharp is not None:
    print(f"Sharp Ratio: {Sharp:.2f}")
print(f"Classificação Final: {classificacao}")
