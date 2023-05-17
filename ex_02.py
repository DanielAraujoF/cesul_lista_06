servico1 = int(input("Informe o servico usado"))
un1 = float(input("Quanto voce usou esse serviço?"))
maisServicos = input("Mais algum serviço foi usado? Digite 1 para SIM, 0 para NÃO")

if servico1 == 1:
    custoHora1 = 0.50
elif servico1 == 2:
    custoHora1 = 0.35
elif servico1 == 3:
    custoHora1 = 0.60
else:
    custoHora1 = 0.20

if maisServicos == 1:
    servico2 = int(input("Informe qual outro serviço voce usou"))
    un2 = float(input("Quanto voce usou esse serviço?"))
    maisServicos_2 = input("Mais algum serviço foi usado? Digite 1 para SIM, 0 para NÃO")

    if servico2 == 1:
        custoHora2 = 0.50
    elif servico2 == 2:
        custoHora2 = 0.35
    elif servico2 == 3:
        custoHora2 = 0.60
    else:
        custoHora2 = 0.20

    if maisServicos_2 == 1:
        servico3 = int(input("Informe qual outro serviço voce usou"))
        un3 = float(input("Quanto voce usou esse serviço?"))

        if servico3 == 1:
            custoHora3 = 0.50
        elif servico3 == 2:
            custoHora3 = 0.35
        elif servico3 == 3:
            custoHora3 = 0.60
        else:
            custoHora = 0.20



custoTotal2 = custoHora2 * un2

