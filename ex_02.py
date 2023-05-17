qtdeInternet = int(input("Informe o consumo de internet: "))
qtdeLocal = int(input("Informe o consumo das ligações locais: "))
qtdeInterurbano = int(input("Informe o consumo das ligações interurbanas: "))
qtdeTorpedo = int(input("Informe o consumo de torpedos: "))

valorInternet = qtdeInternet * 0.5
valorLocal = qtdeLocal * 0.35
valorInterurbano = qtdeInterurbano * 0.6
valorTorpedo = qtdeTorpedo * 0.2

semDesconto = float(valorInternet + valorLocal + valorInterurbano + valorTorpedo)

descontoAtual = 0
tipoDescontoAtual = " "
if qtdeInternet > 50:
    descontoInternet = qtdeInternet * 0.05
    descontoAtual = descontoInternet
    tipoDescontoAtual = "internet"

if qtdeLocal > 200:
    descontoLocal = qtdeLocal * 0.1
    if descontoLocal > descontoAtual:
        descontoAtual = descontoLocal
        tipoDescontoAtual = "local"

if qtdeInterurbano > 150:
    descontoInterurbano = qtdeInterurbano * 0.1
    if descontoInterurbano > descontoAtual:
        descontoAtual = qtdeInterurbano
        tipoDescontoAtual = "interurbano"

if qtdeTorpedo > 50:
    descontoTorpedo = qtdeTorpedo * 0.2
    if descontoTorpedo > descontoAtual:
        descontoAtual = descontoTorpedo
        tipoDescontoAtual = "torpedo"

print(f"O valor sem desconto é {semDesconto:.0f}")
print(f"O valor de cada desconto é: {descontoInternet:.0f}\ {descontoInternet:.0f} ")
o valor total com o desconto atual


# if descontoInternet > descontoLocal and \
#         descontoInternet > descontoInterurbano and \
#         descontoInternet > descontoTorpedo:
#     print("O desconto será sobre o serviço internet")
# elif descontoLocal > descontoInternet and \
#         descontoLocal > descontoInterurbano and \
#         descontoLocal > descontoTorpedo:
#     print("O desconto será sobre o serviço ligação Local")
# elif descontoInterurbano > descontoInternet and \
#         descontoInterurbano > descontoLocal and \
#         descontoInterurbano > descontoTorpedo:
#     print("O desconto será sobre o serviço Ligação interurbana")
# elif descontoTorpedo > descontoInternet and \
#         descontoTorpedo > descontoLocal and \
#         descontoTorpedo > descontoInterurbano:
#     print("O desconto será sobre o serviço torpedo")
# else:
#     print("Não haverá desconto")
#
# print = (f"O valor da fatura será: \n {valorInternet}")