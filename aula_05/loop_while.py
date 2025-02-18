import time
import random

sabores = ["Calabresa", "Frango com catupiry", "Mussarela", "Portuguesa"]

while True:
    i = random.randint(0,3)
    print(sabores[i])
    time.sleep(0.1)
    