#definição de itens e listas.
def espaço():
    print(' ')

def linha():
    print('--'*30)

lista_valor = list()

# Boas-vindas e nome de usuário
# print('Seja bem-vindo ao nosso conversor de escala termométrica.')
# nome = str(input('Por favor digite seu nome: '))
# espaço()
# print('Seja bem-vindo(a)',nome,'vamos começar.')
# espaço()

# Verificação de valor digitado
while True:
    valor = float(input('Digite o valor para  converção: '))

    if valor not in lista_valor:
        lista_valor.append(valor)

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
                    cel_kel = valor + 273.15
                    cel_fah = (valor * 9) / 5 + 32
                    lista_valor.append([cel_kel, cel_fah])
                    print('''O valor convertido de:
                    Celsius para Kelvin é = {:.1f} K
                    Celsius para Fahrenheit é = {:.1f} ºF'''.format(cel_kel, cel_fah))
                    espaço()

                elif escolha == 2:
                    kel_cel = valor -273.15
                    kel_fah = ((valor - 273.15) / 5) * 9 + 32
                    lista_valor.append([kel_cel, kel_fah])
                    print('''O valor convertido de:
                    Kelvin para Celsius é = {:.1f} ºC
                    Kelvin para Fahrenheit é = {:.1f} ºF'''.format(kel_cel, kel_fah))
                    espaço()

                elif escolha == 3:
                    fah_cel = ((valor - 32) / 9) * 5
                    fah_kel = ((valor - 32) / 9) * 5 + 273
                    lista_valor.append([fah_cel, fah_kel])
                    print('''O valor convertido de:
                    Fahrenheit para Celsius é = {:.1f} ºC
                    Fahrenheit para Kelvin é = {:.1f} K'''.format(fah_cel, fah_kel))
                    espaço()

                elif escolha == 4:
                    valor = float(input('Qual valor você deseja converter? '))
                    if valor not in lista_valor:
                        lista_valor.append(valor)
                    espaço()

                elif escolha == 5:
                    # print(lista_valor)
                    print(f'{"No. Digitado"}{"Celsius":>10}{"Kelvin":>10}{"Fahrenheit":>15}')
                    for i in enumerate(lista_valor):
                        print(str(i['0']))
                    # espaço()

                elif escolha == 6:
                    print('Finalizando.....')

                else:
                    print('Opção errada, tente outra vez.')

        print('Fim do programa! Volte sempre!')
        break

