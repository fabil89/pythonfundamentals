# -*- coding: utf-8 -*-

# dados = {
#     'estados': {
#         'sp': {
#             'nome': 'São Paulo',
#             'municipios': 645,
#             'população': 44.04
#         },
#         'rj': {
#             'nome': 'Rio de Janeiro',
#             'municipios': 92,
#             'população': 16.72

#         },
#         'mg': {
#             'nome': 'Minas Gerais',
#             'municipios': 31,
#             'população': 20.87
#         }
#     }
# }


# #Imprima as seguintes informações:


# # 1 - Nome dos Estados


# nome_sp = dados['estados']['sp']['nome']
# nome_rj = dados['estados']['rj']['nome']
# nome_mg = dados['estados']['mg']['nome']

# print(f'O nome dos estados são: {nome_sp}, {nome_rj}, {nome_mg}')
# # #ou
# print('O nome dos estados são:{}, {}, {}\n'.format(nome_sp, nome_rj, nome_mg))




# # Formato:

# #         Nome: nome do estados

# # # 2 - Nome dos estados e sua populações em milhões

# # Formato:
# #         Nome: nome do estado, População: a quantidade

# pop_sp = dados['estados']['sp']['população']
# pop_rj = dados['estados']['rj']['população']
# pop_mg = dados['estados']['mg']['população']

# print(f'A população de {nome_sp} é de {pop_sp} pessoas')
# print(f'A população do {nome_rj} é de {pop_rj} pessoas')
# print(f'A população de {nome_mg} é de {pop_mg} pessoas\n')



# # # 3 - Nome dos estados e quantidade de municipios 

# # Formato:
# #  Nome: nome do estado, Muncipios: a quantidade


# municipio_sp = dados['estados']['sp']['municipios']
# municipio_rj = dados['estados']['rj']['municipios']
# municipio_mg = dados['estados']['mg']['municipios']

# print(f'O estado {nome_sp} possui {municipio_sp} municipios')
# print(f'O estado {nome_rj} possui {municipio_rj} municipios')
# print(f'O estado {nome_mg} possui {municipio_mg} municipios')




# idade = int(input('Digite sua idade: '))
# habilitacao = int(input('Possui Habilitação\n1- para sim\n2- para não\n > '))

# if idade >= 18 and habilitacao == 1:
#     print('Você pode dirigir')
# else:
#     print('Você não pode dirigir')




# frutas = ['banana','abacaxi','maracuja']

# if 'caju' in frutas:
#     print('a lista frutas possui caju')
# else:
#     print('a lista frutas não posui caju')


usuarios = ['rafael','camila','paulo','pamela']

nome = input('Digite o nome do usuário: ')
if nome.lower() in usuarios:
    print('Acesso permitido')
else:
    print('Acesso negado')

