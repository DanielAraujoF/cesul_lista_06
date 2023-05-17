qtdeInternet = int(input("Informe o consumo de internet: "))
qtdeLocal = int(input("Informe o consumo das ligações locais: "))
qtdeInterurbano = int(input("Informe o consumo das ligações interurbanas: "))
qtdeTorpedo = int(input("Informe o consumo de torpedos: "))

valorInternet = qtdeInternet * 0.5
valorLocal = qtdeLocal * 0.35
valorInterurbano = qtdeInterurbano * 0.6
valorTorpedo = qtdeTorpedo * 0.2

semDesconto = valorInternet + valorLocal + valorInterurbano + valorTorpedo

if qtdeInternet > 50:
    descontoInternet = qtdeInternet * 0.05
else:
    descontoInternet = 0
if qtdeLocal > 200:
    descontoLocal = qtdeLocal * 0.1
else:
    descontoLocal = 0
if qtdeInterurbano > 150:
    descontoInterurbano = qtdeInterurbano * 0.1
else:
    descontoInterurbano = 0
if qtdeTorpedo > 50:
    descontoTorpedo = qtdeTorpedo * 0.2
else:
    desconto = 0

if descontoInternet > descontoLocal and\
    descontoInternet > descontoInterurbano and\
    descontoInternet > descontoTorpedo:
    print ("O desconto será sobre o serviço internet")
elif descontoLocal > descontoInternet and\
    descontoLocal > descontoInterurbano and\
    descontoLocal > descontoTorpedo:
    print ("O desconto será sobre o serviço ligação Local")
elif descontoInterurbano > descontoInternet and\
    descontoInterurbano > descontoLocal and\
    descontoInterurbano > descontoTorpedo:
    print("O desconto será sobre o serviço Ligação interurbana")
elif descontoTorpedo > descontoInternet and\
    descontoTorpedo > descontoLocal and\
    descontoTorpedo > descontoInterurbano:
    print ("O desconto será sobre o serviço torpedo")
else:
    print ("Não haverá desconto")

print = (f"O valor da fatura será: \n {valorInternet}")