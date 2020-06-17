print("Bem vindo nosso controle de acesso ")
lista1 = []
lista2 = []
#lista1 é uma lista temporaria
#lista2 é uma lista principal
maior = menos = 0
#Controle de maior e menor idade
while True:
    lista1.append(str(input("Digite o nome: ")))
    lista1.append(int(input("Digite a idade: ")))
#Condição para estabelecar qual a maior e menor idade
    if len (lista2) == 0:
        maior = menor = lista1[1]
    else:
        if lista1[1] > maior:
            maior = lista1[1]
        if lista1[1] < menor:
            menor = lista1[1]
    lista2.append(lista1[:])
    lista1.clear ()
    prox = str(input("Quer cadastrar outra pessoa? S/N "))
    if prox in "Nn":
        break
print("--"*30)
print(f"Entraram no nosso estabelecimento {len (lista2)} pessoas")
print(f"Lista geral",lista1)



print("--"*30)
#Lista das pessoas com menor idade
print(f"A menor idade foi de {menor} anos.")
print()
for p in lista2:
    if p[1] == menor:
        print(f"{p[0]}")
print()
print("--"*30)
#Lista das pessoas com maior idade
print(f"A maior idade foi de {maior} anos.")
print()
for p in lista2:
    if p[1] == maior:
        print(f"{p[0]}")
