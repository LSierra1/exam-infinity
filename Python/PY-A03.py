# Em questions.ipynb (nesta mesma pasta) há mais informações.
pessoas = {
    "João": 23,
    "Maria": 28,
    "Pedro": 35,
    "Lucas": 19,
    "Ana": 16,
    "Mariana": 45,
    "Gabriel": 14,
    "Larissa": 30,
    "Carlos": 40,
    "Tatiana": 22,
    "Rafael": 26,
    "Sofia": 17,
    "Luiz": 21,
    "Patricia": 39,
    "Gustavo": 18,
    "Daniela": 27,
    "Fernando": 33,
    "Camila": 20,
    "José": 50,
    "Roberta": 29,
    "Laura": 15,
    "Antônio": 13,
    "Marcos": 12
}
idade_joao = 0
pessoasMaiorIdade = dict()
pessoasMenorIdade = dict()

idade_joao += pessoas.get("João") # Transfere a idade de João para uma variável chamada "idade_joao".

pessoas["Ana"] = 31 # Adiciona uma pessoa chamada "Ana" com o valor 31 (31 anos).

# Aqui começa uma função para separar as pessoas que tem mais de 18 anos das que tem menos de 18 anos.
def maior_idade(pessoas):

    for nome, idade in pessoas.items():
        if idade >= 18:
            pessoasMaiorIdade[nome] = idade
        else:
            pessoasMenorIdade[nome] = idade

    return pessoasMaiorIdade, pessoasMenorIdade

# Chama a função 'maior_idade(pessoas)' para que os valores de return 'pessoasMaiorIdade' e 'pessoasMenorIdade' sejam armazenadas separadamente fora da função.
pessoasMaiorIdade, pessoasMenorIdade = maior_idade(pessoas)

# Imprime separadamente cada pessoa que tenha mais de 18 anos e menos de 18 anos (bloco criado para uma melhor visualização do resultado final).
print("Pessoas +18:")
for nome, idade in pessoasMaiorIdade.items():
    print(f"Nome: {nome} || Idade: {idade}")
print("------------------------------------------------------------------\n"
      "Pessoas -18:")
for nome, idade in pessoasMenorIdade.items():
    print(f"Nome: {nome} || Idade: {idade}")
print("------------------------------------------------------------------")
print(
    f"Ana foi adicionada a lista de pessoas com o valor '{pessoas['Ana']}' anos.\n"
    f"A idade de João é de {idade_joao} anos.\n" 
      )