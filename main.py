# Instalação necessária:
# pandas (integração do Python com Excel)
# openpyxl (integração do Python com Excel)
# twilio (integração do Python com SMS)

# importar pandas e renomear como pd
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACec371679376c4b850561658f82acda14"
# Your Auth Token from twilio.com/console
auth_token  = "f21dff7605170e9d5882df0ecfe504d6"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # Método para ler arquivo excel e formatar nome para mudar conforme muda o mês
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

        message = client.messages.create(
            to="+5512991161273",
            from_="+17159089780",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)




# Para cada arquivo:

# Verificar se algum valor na coluna Venda daquele arquivo é maior que 55.000

# Se for maior que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada