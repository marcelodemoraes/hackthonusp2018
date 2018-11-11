import csv
import re


with open("raw_bandeco.txt", "r") as rawData:
    data = rawData.readlines() #pegando lista crua

with open('bandeco.csv', 'w', newline='') as csvfile:
    mywriter = csv.writer(csvfile)
    mywriter.writerow(('Periodo', 'DiaSemana', 'PratoPrincipal', 'Vegetariano', 'Guarnicao', 'Sobremesa', 'Fruta', 'ValorEnergetico'))
    counter = 1
    for i in data:
        i = i.replace('Arroz/Feijão/Arroz Integral/\n', '')
        i = i.replace(':sunny:', '')
        i = i.replace(':school:', '')
        i = i.replace(':crescent_moon:', '')
        i = i.replace('Saladas Diversas/\n', '')
        i = i.replace('Opção Vegetariana: ', '')
        i = i.replace('Sobremesa: ', '')
        i = i.replace('Valor energético médio: ⚡️ ', '')
        i = i.replace('Mini pão', '')
        i = i.replace('Minipão', '')
        i = i.replace('Suco', '')
       # i = re.sub("Suco .*$", "", i)
        i = i.replace('São Carlos, Área 1', '')
        i = i.replace('\n', '')
        i = re.sub("\(.*\)", "", i)
        #i = re.sub("Valor energético médio: ⚡️.*$", "", i)
        i = re.sub(".*Kcal", "", i)
        i = i.translate({ord(c): None for c in ':/⚡️🏫🌙🍽☀'}) #limpado chars
        print("counter = " + str(counter) + "  " + "i: " + i)

        if i.strip():
            if counter == 1: #periodo e dia da semana
             #   print("a" + i + "b", end = '')
                simpleList = i.split()
                periodo = simpleList[0]
                diaSemana = simpleList[2]
             #   print(periodo + diaSemana)

            elif counter == 2:
                pratoPrincipal = i

            elif counter == 3:
                veg = i

            elif counter == 4:
                guarnic = i

            elif counter == 5:
                sobremesa = i

            elif counter == 6:
                fruta = i

            elif counter == 6:
                fruta = i

            counter+=1
        if counter > 6:
            counter = 1
            mywriter.writerow((periodo, diaSemana, pratoPrincipal, veg, guarnic, sobremesa, fruta))


