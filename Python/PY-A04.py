# Em questions.ipynb (nesta mesma pasta) há mais informações.

num01 = float(input("Digite um número: "))
num02 = float(input("Digite outro número: "))

while num01 == num02:
    num02 = float(input("Os números não poderão ser iguais. Por favor, digite outro número: "))

print("\n")

def maior_numero(num01, num02):
    return f"{num01} é maior que {num02}" if num01 > num02 else f"{num02} é maior que {num01}."

def maior_numeroMax(num01, num02):
    return f"O maior número entre {num01} e {num02} é {max(num01, num02)}."
# Se "def" não tiver um "return", não é função, e sim procedimento.

resposta01 = maior_numero(num01, num02)
resposta02 = maior_numeroMax(num01, num02)

print(resposta01,
      "\n==========================================\n",
      resposta02)