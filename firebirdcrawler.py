# C:\Users\gpmag\Desktop\pacientes.txt
# nome = input('Digite o nome do arquivo a ser verificado: ')
temp = open('C:\\Users\\gpmag\\Desktop\\temp.tmp', 'r+')
resultado = open('C:\\Users\\gpmag\\Desktop\\resultado.txt', 'a+')
arquivo = open('C:\\Users\\gpmag\\Desktop\\pacientes.txt', 'r')
limite = 10
headers = []
line_counter, col_counter, i = 0, 0, 0
carac_ant = []
limitador = 0
tabulado = False
a = False
for linha in arquivo:
    limitador+=1
    if limitador >= 10:
        break
        #exit()
    else:        
        if linha.strip() == '\n':
            continue
        else:
            temp.write('\n')

            i=0
            campo = ''
            for caractere in linha:
                if caractere != ' ':
                    tabulado = False
                if len(carac_ant) < 5:
                    carac_ant.append(caractere)
                else:
                    carac_ant[4] = caractere
                    a = carac_ant[4] == ' '
                    if carac_ant[4].isnumeric() and caractere == ' ':
                        temp.write('\t')
                        continue

                if i > 2:
                    for j in range(len(carac_ant)):
                        if j < len(carac_ant)-1:
                            carac_ant[j] = carac_ant[j+1]

                i+=1

                

                if caractere == '\n' or caractere == '=':
                    continue
                elif carac_ant.count(' ') > 4 and tabulado == False:
                    temp.write('\t')
                    tabulado = True
                elif caractere != ' ' and tabulado == False or tabulado == False and a:
                    temp.write(caractere)




arquivo.close()
linha = ''
limitador=0
for linha in temp:
    limitador+=1
    line_counter+=1
    if limitador >= 10:
        temp.close()
        resultado.close()
        exit()
    else:        
        for palavra in linha.split():
            if palavra not in headers and line_counter == 3:
                headers.append(palavra)

print(headers)
