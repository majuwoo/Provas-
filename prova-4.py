#Maria Júlia Da Silva
#0220482523039
print("Maria Julia Da Silva, RA: 0220482523039 ")

P = float(input("Digite o valor inicial do investimento: "))
T = int(input("Digite o prazo do investimento em meses: "))
if T < 6:
    J = 0.005 
    J = 0.008 
else:
    J = 0.012 
Rendimento_Total = P * J * T
print(f"\nTaxa de juros mensal aplicada: {J*100:.2f}%")
print(f"Rendimento total obtido: R$ {Rendimento_Total:.2f}")
