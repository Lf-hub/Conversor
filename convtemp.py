from prettytable import PrettyTable
from tkinter import ttk
from tkinter import *

root = Tk()


# status = True
# status_menu = "opcao"
# valores = list()
# itens = list()
# table = PrettyTable()
# table.field_names = [" Vlr Digitado", "Celsius", "Kelvin", "Fahrenheit"]


# def conversor_add_table(data):
#     valor = data.get('valor')
#     calculos = data.get('calculos')

#     if valor not in valores:
#         celsius = calculos.get('celsius')
#         kelvin = calculos.get('kelvin')
#         fahrenheit = calculos.get('fahrenheit')
#         table.add_row([valor, celsius, kelvin, fahrenheit])
#         valores.append(valor)


class Aplication ():

    def __init__(self):
        self.root = root
        self.tela()
        self.start_frame()
        self.botoes()
        root.mainloop()
        
    def tela (self):
        self.root.title('SISTEMA DE CONVERÇÃO')
        self.root.configure(background = 'black')
        self.root.geometry('400x400')

    def start_frame (self):
        
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = 'blue', highlightthickness = 3 )

        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.46)

        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = 'blue', highlightthickness = 3 )
        
        self.frame_2.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.46)

    def botoes(self):
        self.bt_kel = Button(self.frame_1, text = 'kelvin', bd = 3)
        self.bt_kel.place(relx = 0.7, rely = 0.1, relwidth = 0.3, relheight = 0.15)
        
        self.bt_cel = Button(self.frame_1, text = 'Celsius', bd = 3)
        self.bt_cel.place(relx = 0.7, rely = 0.3, relwidth = 0.3, relheight = 0.15)

        self.bt_far = Button(self.frame_1, text = 'Fahrenheit', bd = 3)
        self.bt_far.place(relx = 0.7, rely = 0.5, relwidth = 0.3, relheight = 0.15)

        self.bt_lista = Button(self.frame_1, text = 'Resultados', bd = 3)
        self.bt_lista.place(relx = 0.7, rely = 0.7, relwidth = 0.3, relheight = 0.15)

        
               
        self.kelvin_entry = Entry(self.frame_1)
        self.kelvin_entry.place(relx = 0.07,  rely = 0.1, relwidth = 0.50)
        
        self.cel_entry = Entry(self.frame_1)
        self.cel_entry.place(relx = 0.07,  rely = 0.3, relwidth = 0.50)

        self.far_entry = Entry(self.frame_1)
        self.far_entry.place(relx = 0.07,  rely = 0.5, relwidth = 0.50)






Aplication()


# while True:
#     while status == True:
#         if status_menu == "opcao":
#             print(''' 
#                             MENU
                         
#                 1. Digite um valor para conversão.
#                 2. Exibir tabela de resultados.
#                 3. Sair do programa
#                 ''')
#             escolha = int(input('''
#                 Escolha uma das opção e tecle enter: '''))

#             if escolha == 1:
#                 status_menu = "operacao"
#                 break

#             elif escolha == 2:
#                 print(table)
#                 break

#             elif escolha == 3:
#                 status = False

#             else:
#                 print('Opção errada, tente outra vez.')

#         elif status_menu == "operacao":

#             valor = float(input('''
#                 Digite o valor que você deseja converter? '''))

#             print('''      
#                 Em qual escala está o valor digitado?              
#                        --------------
#                         1. Celsius
#                         2. Kelvin 
#                         3. Fahrenheit 
#                        --------------''')

#             escolha = int(input('''
#                 Escolha uma opção e tecle enter: '''))

#             if escolha == 1:
#                 cel_kel = '{:.2f}'.format(valor + 273.15)
#                 cel_fah = '{:.2f}'.format((valor * 9) / 5 + 32)
#                 data = {"valor": valor, "calculos": {"kelvin": cel_kel, "fahrenheit": cel_fah},}
#                 conversor_add_table(data)
#                 print('''
#                 O valor convertido de:
#                 Celsius para Kelvin é = {} K
#                 Celsius para Fahrenheit é = {}ºF'''.format(cel_kel, cel_fah))
#                 espaco()
#                 resposta = str(input(''''
#                 Deseja continuar? [S/N]'''))

#                 if resposta in 'Ss':
#                     status_menu = 'opcao'
#                     break

#                 else:
#                     if resposta in 'Nn':
#                         print(table)
#                     print('''
#                     Fim do programa! Volte sempre!''')
#                     status = False

#             elif escolha == 2:
#                 kel_cel = '{:.2f}'.format(valor - 273.15)
#                 kel_fah = '{:.2f}'.format(((valor - 273.15) / 5) * 9 + 32)
#                 data = {"valor": valor, "calculos": {"celsius": kel_cel, "fahrenheit": kel_fah}, }
#                 conversor_add_table(data)
#                 print('''
#                 O valor convertido de:
#                 Kelvin para Celsius é = {} ºC
#                 Kelvin para Fahrenheit é = {} ºF'''.format(kel_cel, kel_fah))
#                 espaco()
#                 resposta = str(input('''
#                 Deseja continuar? [S/N]'''))

#                 if resposta in 'Ss':
#                     status_menu = 'opcao'
#                     break

#                 else:
#                     if resposta in 'Nn':
#                         print(table)
#                     print('''
#                     Fim do programa! Volte sempre!''')
#                     status = False

#             elif escolha == 3:
#                 fah_cel = '{:.2f}'.format((valor-32) / 1.8)
#                 fah_kel = '{:.2f}'.format(((valor - 32) / 9) * 5 + 273)
#                 data = {"valor": valor, "calculos": {"celsius": fah_cel, "kelvin": fah_kel}, }
#                 conversor_add_table(data)
#                 print('''
#                 O valor convertido de:
#                 Fahrenheit para Celsius é = {} ºC
#                 Fahrenheit para Kelvin é = {} K'''.format(fah_cel, fah_kel))
#                 espaco()
#                 resposta = str(input('''
#                 Deseja continuar? [S/N]'''))

#                 if resposta in 'Ss':
#                     status_menu = 'opcao'
#                     break

#                 else:
#                     if resposta in 'Nn':
#                         print(table)
#                     print('''
#                     Fim do programa! Volte sempre!''')
#                     status = False

#             else:
#                 print('Opção errada, tente outra vez.')

#     if status == False:
#         break

