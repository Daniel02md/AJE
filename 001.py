from python_percentage import decrement
from csv import writer



nome = input("Nome: ")
idade = int(input("Idade: "))
email = input("Email: ")
telefone = int(input("Telefone: "))

custo = float(input("Custo do projeto: "))
percentual_de_lucro =  custo - decrement(float(input("Qual o percentual de lucro desejado: ")), custo)



CREDITO_TOTAL = 6000

credito_final = CREDITO_TOTAL - custo

estimativa_de_lucro_necessário = custo + percentual_de_lucro
lucro = percentual_de_lucro



with open('cadastros.csv', 'a') as csvfile:
    spamwriter = writer(csvfile, delimiter=',')
    spamwriter.writerow([nome, idade, email, telefone, custo, lucro, estimativa_de_lucro_necessário])


print(f"""

Nome : {nome}
Idade: {idade}
Email: {email}
Telefone: {telefone}
Valor Investido: R${custo:.2f}
Lucro necessário: {estimativa_de_lucro_necessário:.2f}
Crédito disponível: R${credito_final:.2f}

---------------------------------------------------------------------------------------------------
Lucro obtido: {lucro:.2f}
""")
