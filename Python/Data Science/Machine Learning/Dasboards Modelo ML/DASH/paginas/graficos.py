
# Não roda uma aplicação/servidor do DASH, apenas define a DIV

from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features
#print(dados.head())

# 1 Histograma:
figura_histograma = px.histogram(dados, x='age', title='Histograma de idades')
#Cria a váriavel que recebe o Div do HTML + Gráfico para quando chamar esta variável reduzir linha de código
div_do_histograma = html.Div([
            #html.H2('Histograma de idades'),
            dcc.Graph(figure=figura_histograma),
        ])


# 2 Boxplot:
dados["doenca"] = (heart_disease.data.targets > 0) * 1
# boxplot das idades por doenca, colorido por doenca
figura_boxplot = px.box(dados, x='doenca', y='age', color='doenca', title='Boxplot de idades')
#Cria a váriavel que recebe o Div do HTML + Gráfico para quando chamar esta variável reduzir linha de código
div_do_boxplot = html.Div([
        #html.H2('Boxplot de idades'),    
        dcc.Graph(figure=figura_boxplot)
    ])

#3 Adicionando na Página

layout = html.Div([
    html.H1('Análise de dados do Repositório UCI de Doenças Cardíacas', className='text-center mb-5'),
        dbc.Container([
            dbc.Row([
                    dbc.Col([div_do_histograma], md=6),
                    dbc.Col([div_do_boxplot], md=6)
        ])
    ])
])

# app.layout.children.append(div_do_boxplot) se quiser pode adicionar de forma dinâmica no layout, porém ficará comentado esta linha.
