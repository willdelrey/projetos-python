nome=(input("qual a pohha do seu nome?" ))
print("ola,{}!!".format(nome))

print("bem vindo ao menu principal")
while menuprincipal=="1":
    print("o que gostaria de fazer hoje?")
    print("1-converter temperaturas.\n2-calcular o preço de uma viagem de taxi.\n3-calcular o preço de alimentos por quilograma.\n0-sair")
    todo=int(input("digite o numero referente à opçao desejada:"))
    if todo==1:
        todo="converter temperaturas"
        print("você escolheu a opção: {}".format(todo))
        tempx=float(input("Por favor, informe-me a temperatura "))
        unimed=str.upper(input("Qual a unidade de medida usada em sua região? Digite a Letra inicial sendo:\nF-fahrenheint\nC-Celsius\nK-Kelvin\n"))
        unimedconv=str.upper(input("Para qual unidade de medida você deseja converter?\n Digite a Letra inicial sendo:\nF-fahrenheint\nC-Celsius\nK-Kelvin\n"))
        #passo 1:C, K->F
        if unimed=="C" and unimedconv=="F":
            cf=tempx*9/5+32
            print("temperatura igual a {}{}.".format(cf, unimedconv ))
        elif unimed=="K" and unimedconv=="F":
            kf=(tempx-273.15)*9/5+32
            print("temperatura igual a {}{}.".format(kf, unimedconv ))
        elif unimed!="F" or unimed!= "K" or unimed!= "C":
            menuprincipal=str(input("deseja voltar ao menu principal?\n digite \n0-SAIR\n 1-VOLTAR AO MENU PRINCIPAL\n"))
            if menuprincipal=="1":
            #passo 2: C, F-> K
        elif unimed=="C" and unimedconv=="K":
            ck=tempx+273.15
            print("temperatura igual a {}{}.".format(ck, unimedconv ))
        elif unimed=="F" and unimedconv=="K":
            fk=(tempx-32)*5/9+273.15
            print("temperatura igual a {}{}.".format(fk, unimedconv ))
            menuprincipal=str(input("deseja voltar ao menu principal?\n digite \n0-SAIR\n 1-VOLTAR AO MENU PRINCIPAL\n"))
            if menuprincipal=="1":
            #passo 3: F, K ->C
        elif unimed=="F" and unimedconv=="C":
            fc=(tempx-32)*5/9
            print("temperatura igual a {}{}.".format(fc, unimedconv ))
        elif unimed=="K" and unimedconv=="C":
            kc=tempx-273.15
            print("temperatura igual a {}{}.".format(kc, unimedconv ))
        elif unimed!="F" or unimed!= "K" or unimed!= "C":
           menuprincipal=str(input("deseja voltar ao menu principal?\n digite \n0-SAIR\n 1-VOLTAR AO MENU PRINCIPAL\n"))
            if menuprincipal=="1":
    if todo==2:
        todo="calcular o preço final de uma viagem de taxi"
        print("você escolheu a opção: {}".format(todo))
        precofx=float(input("Qual o valor fixo da corrida? R$"))
        precovar=float(input("Qual o valor/km? R$"))
        distance=float(input("qual a distância em km? "))
        precofinal=precovar*distance+precofx
        print("preço final: R${:.2f}".format(precofinal))
    elif menuprincipal==0:
        break