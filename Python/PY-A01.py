# Em questions.ipynb (nesta mesma pasta) há mais informações.

quantities = int(input("Digite a quantidade de alunos na turma: "))
accumulator = 0

for i in range(quantities):
    ages = int(input(f"Digite a idade do {i+1}° aluno: "))
    accumulator += ages

print(f"A média de idades da sala (total de {quantities} alunos) é de, aproximadamente, {accumulator / quantities} anos.")