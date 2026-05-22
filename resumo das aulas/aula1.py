"""

1 - atribuição de valor a variavel e sua tipagem
2 - operação matematica e concatenação
3 - input
4 - formatação de mensagem

"texto" # str
1 # int
1.5 # float
True # bool
False # bool


receita: str = "cuzcuz com ovo"
magia: str = "Maldição"
peso: float = 60.2
altura: float = 1.80

novo_valor: float = peso + altura # operação matematica
novo_valor_texto: str = receita + magia # concatenação

nome: str = input("Qual seu nome? ")
idade: int = int(input("Quantos anos você tem? "))

entrada: bool = True

mensagem: str = f"Olá {nome}, você tem {idade} anos.\nSua entrada é: {entrada}" # formatação

print(mensagem)
"""