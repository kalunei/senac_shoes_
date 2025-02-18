"""
 E.X. :
    => No Brasil, para alguém dirigir a pessoa precisa ter 18 anos ou mais.
    => Se a pessoa tiver mais de 18 anos, ela pode dirigir.
    => Se nâo, ela não pode dirigir. 
    => Se ela tiver entre 0 até 17 anos, ela nao pode dirigir.
"""

idade_pessoa = int(input("Digite sua idade: "))

if idade_pessoa >= 18:
    print("Pode dirigir   （＾∀＾●）")
elif idade_pessoa >= 0 and idade_pessoa <= 17:
    print("Nao pode dirigir    ಥ_ಥ")
else:
    print("Informe uma idade valida")
   