from prettytable import PrettyTable


def espaco():
    print(' ')

status = True
status_menu = "opcao"
valores = list()
itens = list()
table = PrettyTable()
table.field_names = [" Vlr Digitado", "Celsius", "Kelvin", "Fahrenheit"]


def conversor_add_table(data):
    valor = data.get('valor')
    calculos = data.get('calculos')

    if valor not in valores:
        celsius = calculos.get('celsius')
        kelvin = calculos.get('kelvin')
        fahrenheit = calculos.get('fahrenheit')
        table.add_row([valor, celsius, kelvin, fahrenheit])
        valores.append(valor)

print('''
             -------------------------------------
             SISTEMA DE CONVERÇÃO  -   versão 1.0
             --------------------------------------''')
while True:
    while status == True:
        if status_menu == "opcao":
            print(''' 
                            MENU
                         
                1. Digite um valor para conversão.
                2. Exibir tabela de resultados.
                3. Sair do programa
                ''')
            escolha = int(input('''
                Escolha uma das opção e tecle enter: '''))

            if escolha == 1:
                status_menu = "operacao"
                break

            elif escolha == 2:
                print(table)
                break

            elif escolha == 3:
                status = False

            else:
                print('Opção errada, tente outra vez.')

        elif status_menu == "operacao":

            valor = float(input('''
                Digite o valor que você deseja converter? '''))

            print('''      
                Em qual escala está o valor digitado?              
                       --------------
                        1. Celsius
                        2. Kelvin 
                        3. Fahrenheit 
                       --------------''')

            escolha = int(input('''
                Escolha uma opção e tecle enter: '''))

            if escolha == 1:
                cel_kel = '{:.2f}'.format(valor + 273.15)
                cel_fah = '{:.2f}'.format((valor * 9) / 5 + 32)
                data = {"valor": valor, "calculos": {"kelvin": cel_kel, "fahrenheit": cel_fah},}
                conversor_add_table(data)
                print('''
                O valor convertido de:
                Celsius para Kelvin é = {} K
                Celsius para Fahrenheit é = {}ºF'''.format(cel_kel, cel_fah))
                espaco()
                resposta = str(input(''''
                Deseja continuar? [S/N]'''))

                if resposta in 'Ss':
                    status_menu = 'opcao'
                    break

                else:
                    if resposta in 'Nn':
                        print(table)
                    print('''
                    Fim do programa! Volte sempre!''')
                    status = False

            elif escolha == 2:
                kel_cel = '{:.2f}'.format(valor - 273.15)
                kel_fah = '{:.2f}'.format(((valor - 273.15) / 5) * 9 + 32)
                data = {"valor": valor, "calculos": {"celsius": kel_cel, "fahrenheit": kel_fah}, }
                conversor_add_table(data)
                print('''
                O valor convertido de:
                Kelvin para Celsius é = {} ºC
                Kelvin para Fahrenheit é = {} ºF'''.format(kel_cel, kel_fah))
                espaco()
                resposta = str(input('''
                Deseja continuar? [S/N]'''))

                if resposta in 'Ss':
                    status_menu = 'opcao'
                    break

                else:
                    if resposta in 'Nn':
                        print(table)
                    print('''
                    Fim do programa! Volte sempre!''')
                    status = False

            elif escolha == 3:
                fah_cel = '{:.2f}'.format((valor-32) / 1.8)
                fah_kel = '{:.2f}'.format(((valor - 32) / 9) * 5 + 273)
                data = {"valor": valor, "calculos": {"celsius": fah_cel, "kelvin": fah_kel}, }
                conversor_add_table(data)
                print('''
                O valor convertido de:
                Fahrenheit para Celsius é = {} ºC
                Fahrenheit para Kelvin é = {} K'''.format(fah_cel, fah_kel))
                espaco()
                resposta = str(input('''
                Deseja continuar? [S/N]'''))

                if resposta in 'Ss':
                    status_menu = 'opcao'
                    break

                else:
                    if resposta in 'Nn':
                        print(table)
                    print('''
                    Fim do programa! Volte sempre!''')
                    status = False

            else:
                print('Opção errada, tente outra vez.')

    if status == False:
        break

