nome: str = "Fatz"

for caracter in nome: # iterar para cada condição True
    print(caracter)
else:
    print("Nome sem caracteres...") # caso condição False, caimos no bloco do else, exemplo: nome: str = "" (não possui caracteres)

# toda iteração acontece em blocos controlados por True, sendo assim, o desenvolvedor sempre deve saber em cima do que está trabalhando, seja através do tipo do objeto ou por um novo objeto, exemplos:

anos: list[int] = [1997, 1998, 1999, 2000, 2001, 2002] # objeto -> lista de inteiros
novo_anos: list[int] = [ano for ano in anos if ano >= 2000] # novo objeto -> lista de inteiros a partir de uma nova condição True

# o mesmo se aplica em while, condição True + saída False, exemplo:

while True:
    ...
else: # False
    ...