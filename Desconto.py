preco_total : float
desconto : float
preco_desconto : float
preco_final : float
nome_produto : str

nome_produto = input("Qual é o produto a ser aplicado o desconto?")
preco_total = float(input("Qual é o preço original do produto?"))
desconto = float(input("Qual é o desconto a ser aplicado em porcentagem?"))

preco_desconto = (preco_total * (desconto / 100))
preco_final = (preco_total - preco_desconto)

if preco_final > 1000 :
    print ("Está muito caro!")
elif preco_final > 800 and preco_final <= 1000 :
    print ("Está caro!")
elif preco_final > 500 and preco_final <= 800 :
    print ("Preço Justo")
else :
    print ("Está Barato!")

print ("O valor de ", nome_produto, " com o desconto aplicado é de ", preco_final," reais.")
