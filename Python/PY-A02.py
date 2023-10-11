# Em questions.ipynb (nesta mesma pasta) há mais informações.

numbers1 = list()
numbers2 = []

while True:
    print('Para prosseguir com a próxima lista, digite "END".')
    addNumber1 = input("Digite um número para adicionar na 1° lista: ")
    for i in numbers1:
        while i == addNumber1:
            addNumber1 = input(f"Número {addNumber1} já na lista. Digite outro número: ")
    while addNumber1.isalpha() and addNumber1.upper() != "END":
        addNumber1 = input("Por favor, digite um número: ")
    if addNumber1.isdigit():
        numbers1.append(addNumber1)
    elif not numbers1:
        print("Você não inseriu nenhum número na lista.")
        exit()
    elif addNumber1 not in "1234567890" and addNumber1.upper() == "END":
        break

print("Agora vamos para a segunda lista. Você poderá inserir os mesmos números que inseriu na lista anterior, porém apenas uma única vez.")

while True:
    print('Para parar de adicionar números, digite "END".')
    addNumber2 = input("Digite um número para adicionar na 2° lista: ")
    for j in numbers2:
        while j == addNumber2:
            addNumber2 = input(f"Número {addNumber2} já na lista. Digite outro número: ")
    while addNumber2.isalpha() and addNumber2.upper() != "END":
        addNumber2 = input("Por favor, digite um número: ")
    if addNumber2.isdigit():
        numbers2.append(addNumber2)
    elif not numbers2:
        print("Você não inseriu nenhum número na lista.")
        exit()
    elif addNumber2 not in "1234567890" and addNumber2.upper() == "END":
        break

commonNumbers = []
soma = 0

for numberCheck1 in numbers1:
    for numberCheck2 in numbers2:
        if numberCheck1 == numberCheck2:
            commonNumbers.append(numberCheck1)
            soma += int(numberCheck1) # Por algum motivo, o código dá erro caso eu não converta o numberCheck1 para int

print("Lista 1:", numbers1)
print("Lista 2:", numbers2)
print("Números em comum:", commonNumbers)
print("Soma dos números em comum:", soma)
