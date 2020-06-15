from prettytable import PrettyTable

#definição de itens e listas.
def espaço():
    print(' ')

def linha():
    print('--'*30)

valores = list()
itens = list()
table = PrettyTable()
table.field_names = ["No.", " Vlr Digitado", "Celsius", "Kelvin", "Fahrenheit"]

seq = 0

# Verificação de valor digitado

def conversor_add_table(data):

    valor = data.get('valor')
    calculos = data.get('calculos')

    if valor not in valores:
        seq = seq=1
        celsius = calculos.get('celsius')
        kelvin = calculos.get('kelvin')
        fahrenheit = calculos.get('fahrenheit')

        table.add_row([seq, valor, celsius, kelvin, fahrenheit])
        valores.append(valor)



# Boas-vindas e nome de usuário
# print('Seja bem-vindo ao nosso conversor de escala termométrica.')
# nome = str(input('Por favor digite seu nome: '))
# espaço()
# print('Seja bem-vindo(a)',nome,'vamos começar.')
# espaço()

while True:
    valor = float(input('Digite o valor para  converção: '))

# Menu inicial
    escolha = 0
    while escolha != 6:
                print('''
___________________________________
            MENU PRINCIPAL
___________________________________
  Qual escala voçê quer converter?

1. Celsius
2. Kelvin 
3. Fahrenheit 
4. Nova conversão
5. Tabela com resultados
6. Sair deste programa
____________________________________''')
                escolha = int(input('Escolha uma opção e tecle enter: '))
                linha()
                espaço()
                if escolha == 1:
                    cel_kel = '{:.1f}'.format(valor + 273.15)
                    cel_fah = '{:.1f}'.format((valor * 9) / 5 + 32)
                    data = {"valor": valor,
                            "calculos": {
                                "kelvin": cel_kel,
                                "fahrenheit": cel_fah},
                            }
                    conversor_add_table(data)

                    print('''O valor convertido de:
                    Celsius para Kelvin é = {} K
                    Celsius para Fahrenheit é = {}ºF'''.format(cel_kel, cel_fah))
                    espaço()

                elif escolha == 2:
                    kel_cel = '{:.1f}'.format(valor -273.15)
                    kel_fah = '{:.1f}'.format(((valor - 273.15) / 5) * 9 + 32)
                    table.add_row([valor, kel_cel, " ", kel_fah])
                    print('''O valor convertido de:
                    Kelvin para Celsius é = {} ºC
                    Kelvin para Fahrenheit é = {} ºF'''.format(kel_cel, kel_fah))
                    espaço()

                elif escolha == 3:
                    fah_cel = '{:.1f}'.format((valor - 32) / 9) * 5
                    fah_kel = '{:.1f}'.format(((valor - 32) / 9) * 5 + 273)
                    table.add_row([valor, fah_cel, fah_kel, " "])
                    print('''O valor convertido de:
                    Fahrenheit para Celsius é = {} ºC
                    Fahrenheit para Kelvin é = {} K'''.format(fah_cel, fah_kel))
                    espaço()

                elif escolha == 4:
                    break
                    # valor = float(input('Qual valor você deseja converter? '))
                    # if valor not in valores:
                    #     valores.append(valor)
                    # espaço()

                elif escolha == 5:
                    print(table)


                elif escolha == 6:
                    print('Finalizando.....')

                else:
                    print('Opção errada, tente outra vez.')

    print('Fim do programa! Volte sempre!')
    break

