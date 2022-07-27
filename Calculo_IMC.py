#Desenvolvimento de uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
#e mostre seu status, de acordo com a tabela abaixo:

# IMC abaixo de 18,5: Abaixo do Peso

# Entre 18,5 e 25: Peso Ideal

# 25 até 30: Sobrepeso

# 30 até 40: Obesidade

# Acima de 40: Obesidade Mórbida

from time import sleep

import emoji
from emoji import emojize
print("Usuário informe seu peso em Kg: ")
peso=float(input())
print("Agora informe sua altura em metros: ")
altura= float(input())
imc= peso/(altura**2)
print("O IMC do usuário é de {:.2f}" .format(imc))
sleep(1.5)
if imc<18.5:
    print(emoji.emojize('ATENÇÃO... :thumbsdown: :no_entry_sign: ', use_aliases=True ))
    print("ABAIXO DO PESO")
elif imc>=18.5 and imc<=25:
    print(emoji.emojize("PESO IDEAL :wink: :facepunch:", use_aliases=True))
elif imc>25 and imc<=30:
    print(emoji.emojize("SOBREPESO :neutral_face:", use_aliases=True))
else:
    print(emoji.emojize("ATENÇÃO.... :sos:", use_aliases=True))
    print(emoji.emojize("OBESIDADE MÓRBIDA :scream_cat:",use_aliases=True))