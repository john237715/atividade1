#arc
print("Olá meu nome é João Pedro . Seja muito bem vindo(a) a JP Produtos Agrícolas.")
cargo = input("Informe seu atual cargo: ")
salário =float(input("Informe seu salário: "))
anodenascimento=int(input("Informe seu ano de nascimento: "))
from datetime import datetime
hoje = datetime.now()
ano = int(hoje.strftime("%Y"))
idade=(ano - anodenascimento)
limite=salário * (idade / 1000) + 100
print("Seu cargo é: ",cargo)
print("Seu salário: ",salário)
print("Seu ano de nascimento: ",anodenascimento)
print("Sua idade: ",idade,"anos")
print("Seu limite de gasto: ",limite,"reais")
print("Ano: ",ano)
#etapa3
NomeProduto:input("Qual o nome do produto: ")
ValorProduto=float(input("Preço do produto: "))
PorcentagemDoProduto=(ValorProduto * 100) / limite
if PorcentagemDoProduto <=60:
    print("Liberada a compra do produto")
elif 60 < PorcentagemDoProduto <= 90:
    print(" A compra do produto está liberada e pode ser parcelada em até 2x")
elif 90< PorcentagemDoProduto <= 100:
    print(" A compra do produto está liberada e pode ser parcelada em 3x ou mais")
else:
    print(" A compra deste produto não pode ser efetuada, limite não suficiente")
PrimeiroNome = "João"
NomeCompleto = "João Pedro Guimarães de Oliveira"
desconto_na_compra = (ValorProduto * len(PrimeiroNome)) / 100
Produto_com_desconto_aplicado= ValorProduto - desconto_na_compra
if ValorProduto >= len(NomeCompleto) <= idade:
    print("Você terá um desconto de 4% em sua compra")
    print("O valor do produto com o desconto de nossa loja é: ",Produto_com_desconto_aplicado)
print("Parabéns pela compra efetuada!")
