'''
2. **Verificação de Ingredientes**
Dado dois conjuntos de ingredientes, `exiba os ingredientes comuns entre eles` e os `que estão disponíveis apenas em um conjunto.`
'''

ingredientes_lactose = {"leite", "manteiga", "queijo", "leite_condensado", "bolo"}
ingredientes_mt_gordurosos = {"manteiga", "óleo" ,"queijo", "pastel", "ovo" }


ingredientes_comuns = ingredientes_lactose.intersection(ingredientes_mt_gordurosos)
ingredientes_total = ingredientes_lactose.union(ingredientes_mt_gordurosos)
ingredientes_solo = ingredientes_lactose.difference(ingredientes_mt_gordurosos)

print("Ingredientes comuns entre eles:", ingredientes_comuns)
print("Disponíveis apenas em um conjunto:", ingredientes_solo)