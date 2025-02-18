# P I Z Z A R I A    S A B O R A S 
# Calabresa, 4queijos, Frango com Requeijão.
# Se o cliente pedir uma piza de calabresa, na sexta feira o refri é cortezia
# Se o cliente pedir qualquer pizza no sabado o frete é gratis, Senão informe ao cliente apenas que a pizza solicitada está sendo preparada.

#var.
barra = ("-"*35)
sabor_pizza = ()
dia_semana = "sexta"
#var.

# menu.
print(f"{barra}🍕🍔🍟🌭 P I Z Z A R I A    S A B O R A S 🍕🍔🍟🌭{barra}")
sabor_pizza = int(input(f""" 
Digite o sabor da pizza que deseja: 
1) Calabresa;
2) 4queijos;
3) Frango com Requeijão.
:"""))
# menu.

# calculos.
if sabor_pizza == 1 and dia_semana == "sexta":
    print("Parabens!!!O refri é cortezia 🥤🧊!")
elif dia_semana == "sabado":
    print("Parabens!!! O frete é gratis 🛵!")
else:
    print("Sem promoções Hoje") 

print("A sua pizza está sendo preparada   (✿◡‿◡) ")
# calculos.
input()