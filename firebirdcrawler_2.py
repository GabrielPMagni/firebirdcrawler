# -*- coding: utf-8 -*-

# C:\Users\gpmag\Desktop\pacientes.txt
# nome = input('Digite o nome do arquivo a ser verificado: ')
nome = 'pacientes.txt'
temp = open('/home/gabriel/Área de trabalho/app/firebirdcrawler-master/temp.tmp', 'r+')
resultado = open('/home/gabriel/Área de trabalho/app/firebirdcrawler-master/resultado.txt', 'a+')
url = '/home/gabriel/Área de trabalho/app/firebirdcrawler-master/'
arquivo = open(url+nome, 'r', encoding='latin-1')
limite = 10
headers = []
line_counter, col_counter, i = 0, 0, 0
carac_ant = []
limitador = 0
campos = []
tabulado = False
a = False
achoutxt = False
nova_coluna = False
campotxt = ''
primeira_coluna = True
x = False  # é espaço único entre um header e outro?
mesmo_texto = True
for linha in arquivo:
    
    line_counter+=1
    limitador+=1
    if limitador >= 10:
        print(campos)
        break
        #exit()
    else:        
        if linha.strip() == '\n':
            continue
        else:
            temp.write('\n')

            i=0
            campo = 0

            for caractere in linha:
                if caractere != ' ':
                    tabulado = False
                if len(carac_ant) < 5:
                    carac_ant.append(caractere)
                else:
                    carac_ant[4] = caractere
                    a = carac_ant[4] == ' '
                    

                if i > 2:
                    for j in range(len(carac_ant)):
                        if j < len(carac_ant)-1:
                            carac_ant[j] = carac_ant[j+1]

                i+=1


                if line_counter == 2:
                    if not primeira_coluna:
                        if caractere == ' ' and nova_coluna:
                            mesmo_texto = False
                            nova_coluna = False
                        elif caractere != ' ' and caractere != '\n':
                            achoutxt = True
                            mesmo_texto = True
                        if caractere == ' ' and achoutxt and mesmo_texto:
                            print(campo)
                            campos.append(campotxt)
                            campotxt=''
                            campo=0
                            achoutxt = True
                            nova_coluna = True
                            mesmo_texto = False
                        elif:
                            campotxt=campotxt+caractere
                            campo+=1
                        x = True

                    elif primeira_coluna:
                        if caractere != ' ' and caractere != '\n':
                            achoutxt = True
                        if caractere == ' ' and achoutxt:
                            print(campo)
                            campos.append(campotxt)
                            campotxt=''
                            campo=0
                            nova_coluna = True
                            primeira_coluna = False
                            continue
                        else:
                            campotxt=campotxt+caractere
                            campo+=1
                


                if caractere == '\n' or caractere == '=':
                    continue
                elif carac_ant.count(' ') > 4 and tabulado == False:
                    temp.write('\t')
                    tabulado = True
                elif caractere != ' ' and tabulado == False or tabulado == False and a:
                    temp.write(caractere)



temp.close()
temp = open('/home/gabriel/Área de trabalho/app/firebirdcrawler-master/temp.tmp', 'r')


arquivo.close()
'''
linha = ''
limitador=0
line_counter=0
for linha in temp:
    limitador+=1
    line_counter+=1
    if line_counter >= 10:
        temp.close()
        resultado.close()
        exit()
    else:        
        for palavra in linha.split():
            if palavra not in headers and line_counter == 3:
                headers.append(palavra)
                resultado.write(palavra+'\t')
            elif line_counter > 3:
                pass


print(headers)
'''
