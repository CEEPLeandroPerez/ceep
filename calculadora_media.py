print("vamos calcular sua media!")
nota1 = float(input("digite a 1°a nota"))
nota2 = float(input("digite a 2°a nota"))
nota3 = nota1 + nota2 % 2

if nota3 >= 70:
    print(f"sua media é {nota3} passou!")
else:
    print(f"sua media é {nota3} nao passou!")                        