### C O N J U N T O S ###
"""
Conjuntos (listas mutáveis)
    ---> Não ordenados; 
    ---> Heterogênios ou Homogênios;
    ---> NÂO permitem elementos duplicados, se usar duplicatas o conjunto lê como apenas 1.
"""

##/ EX:
ingredientes = {"tomate", "alface", "cebola", "tomate"}
print("🥐🥘🥙🍣🌮 : ", ingredientes)
##*/ EX:


##/ Operações com conjuntos :


#/ Adicionar itens; 
ingredientes.add("oregáno")
print("🧇🥞🍟 Ingredientees atualizados:", ingredientes)
#*/ Adicionar itens.

#/ Remover itens; 
ingredientes.remove("tomate")
print("🧇🥞🍟 Ingredientees atualizados:", ingredientes)
#*/ Remover itens.

#/ União de conjuntos;
adicionais = {"bacon", "palmito"}
todos_ingredientes = ingredientes.union(adicionais)
print("🧇🥞🍟 Ingredientees atualizados:", todos_ingredientes)
#*/ União de conjuntos.

#/ Interceção de conjuntos;
pizza_vegana = {"tomate", "alface", "cebola", "rúcula"}
comuns = ingredientes.intersection(pizza_vegana)
print("🧇🥞🍟 Ingredientees atualizados:", comuns)
#*/ Interceção de conjuntos.


##*/ Operações com conjuntos :