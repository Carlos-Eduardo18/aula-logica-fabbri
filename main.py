# isso é um comentário

# print("oi Senai Suiço-Brasileiro!")

import operacoes

umnumero = int(input("Digite um número inteiro:"))
umataxa = int(input("Digite uma taxa:"))

resultado = operacoes.fatorial(5)
print(f"O fatorial de {umnumero} é {resultado}")

print(f"O triplo de {umnumero} é {operacoes.triplo(umnumero)}")

print(f"Aumentando R$ {umnumero} em {umataxa} é R$ {operacoes.aumentar(umnumero, umataxa)}")

