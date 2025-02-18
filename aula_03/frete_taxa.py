"""Agora, a nossa pizzaria está cobrando uma `taxa fixa de R$5 por entrega`, além de `R$1 por km até 5km,` e `R$2 por km até 10km`. Mais ainda 
`não entregamos com a distância superior a 10km`.

Pegando como base essas possibilidades, faça um programa que responda as seguintes perguntas:

- Quanto Joana irá pagar de frete, sendo que mora a 8km da pizzaria.
- Quanto Guilherme irá pagar de frete, sendo que mora a 3km da pizzaria.
- Quanto Rafael irá pagar de frete, sendo que mora a 11km da pizzaria."""


# var.
distância = int(input("Digite a distância: "))
taxa_f = 5
f = "Frete: "
# var.

# principal.
if distância <= 5:
    valor = taxa_f + (distância*1) 
    print(f + str(valor) + "🛵")
elif distância <= 10 and distância > 5:
    valor = taxa_f + (distância*1) 
    print(f + str(valor) + "🛵")
else: 
    print("Pedido nao pode ser concluido devido a distância (x_x)")
# principal.