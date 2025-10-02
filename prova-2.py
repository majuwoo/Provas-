#Maria Júlia Da Silva
#0220482523039
print("Maria Julia Da Silva, RA: 0220482523039 ")

glicose = float(input("Digite o valor da sua Glicose em jejum: "))
if glicose < 100 :
    print("Glicemia normal. ")
elif glicose >= 100 or glicose >= 125:
    print("Pré-diabetes: Risco Moderado.")
else:
    print("Diabetes: Nível Alto.")
