idade: int = int(input("Qual sua idade? "))
# int() só converte digitos, caso insira qualquer outro caracter um erro será disparado:
# ValueError: invalid literal for int() with base 10: 'A'

# na hora do desenvolvimentos, deixamos que dispare esses tipos de erros para que possamos tratar e então entregar um projeto responsivo:
try:
    idade: int = int(input("Qual sua idade? "))
except ValueError: # Tratamos cada tipo de erro individualmente, evitando que o projeto quebre e o usuário receba um código em vermelho
    print("Insira apenas dígitos.")
else: # O bloco else só será executado em casos que o try foi um sucesso e não teve erros
    print("Sem erros. Idade registrada.")
finally: # Independente se houve ou não erros, finally é um bloco que sempre será executado
    print("Acertos e erros foram processados. A idade pode ter sido ou não registrada. Finalizando...")