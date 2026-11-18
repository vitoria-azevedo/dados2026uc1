#CRIE UM ALGORITIMO PARA DIZER SE UMA PESSOA É MAIOR DE IDADE OU NÃO 
#Número= int ou float
idade = int(input("qual a sua idade? "))

if idade >= 18: 
    print("você é maior de idade")
    print("pode tirar a carteira de motorista")
else: 
    print("você é menor de idade.")
    faltam= 18 - idade
    print(f"faltam {faltam} anos(s) para completar 18 anos.")
   
print("fim do programa.")

