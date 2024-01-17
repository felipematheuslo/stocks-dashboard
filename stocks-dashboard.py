# -*- coding: utf-8 -*-
"""
Created on Jan 10 2024
@author: Felipe Laurindo
"""

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# importar a aba Carteira como DataFrame
planilha_carteira = pd.read_excel("stocks_spreadsheet.xlsx", "Carteira")
# limpeza dos dados
planilha_carteira.drop(axis=0, index=planilha_carteira.index[17:30], inplace=True)

# importar a aba Dividendos como DataFrame
planilha_dividendos = pd.read_excel("stocks_spreadsheet.xlsx", "Dividendos")
df = planilha_dividendos.groupby(planilha_dividendos['Data PGTO'].dt.year).sum('Dividendos')

fig1 = px.pie(planilha_carteira, 
             names='Ticker', 
             values='Total Hoje', 
             title='Alocação por ativo',
             width=600, height=600)

fig1.update_traces(textposition='inside', 
                  textinfo='percent+label',
                  insidetextorientation='radial')

fig2 = px.pie(planilha_carteira, 
             names='Setor', 
             values='Total Hoje', 
             title='Alocação por setor',
             width=600, height=600)

fig2.update_traces(textposition='inside', 
                  textinfo='percent+label')

fig3 = px.bar(df, 
              title='Dividendos por ano', 
              x=df.index, y='Dividendos')

# dashboard no host local http://127.0.0.1:8050
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Dashboard de ações', style={'textAlign':'center'}),
    dcc.Graph(id='graph-content1', figure=fig1),
    dcc.Graph(id='graph-content2', figure=fig2),
    dcc.Graph(id='graph-content3', figure=fig3)
])

if __name__ == '__main__':
    app.run(debug=True)