import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
import numpy as np

import plotly.graph_objects as go


# Dados

dados_conceitos = dict(
    
    Java =          {'variáveis' : 3,   'condicionais' : 6,     'loops' : 2, 'poo' :1,  'funções' :1},
    Python =        {'variáveis' : 9,   'condicionais' : 8,     'loops' : 5, 'poo' :7,  'funções' :4},
    SQL =           {'variáveis' : 10,  'condicionais' : 2,     'loops' : 5, 'poo' :4,  'funções' :6},
    GoLand =        {'variáveis' : 10,  'condicionais' : 10,    'loops' : 9, 'poo' :8,  'funções' :10},
    JavaScript =    {'variáveis' : 8,   'condicionais' : 7,     'loops' : 2, 'poo' :10, 'funções' :4},
    ShellScript =   {'variáveis' : 9,   'condicionais' : 8,     'loops' : 5, 'poo' :7,  'funções' :1},
    PLSQL =         {'variáveis' : 8,   'condicionais' : 5,     'loops' : 3, 'poo' :8,  'funções' :8},
    Cobol =         {'variáveis' : 7,   'condicionais' : 9,     'loops' : 5, 'poo' :3,  'funções' :7},
    PHP =           {'variáveis' : 9,   'condicionais' : 10,    'loops' : 8, 'poo' :1,  'funções' :9},
)


color_map = dict(
    Java = 'red',
    Python = 'blue',
    SQL = 'green',
    GoLand = 'gray',
    JavaScript = 'lightgreen',
    ShellScript = 'yellow',
    PLSQL = 'pink',
    Cobol = 'purple',
    PHP = 'brown'
)

app = dash.Dash(__name__)


#_________________________________Layout_______________________________________
# Sempre que for subir um app para validar, usar o debug abaixo para mapear
# Esses dois "Layout and Callbacks" precisam trabalhar juntos

app.layout = html.Div([
    html.H1('Anderson Ferreira', style={'text-align':'center'}),
    html.H2('Built your steps', style={'text-align':'center'}),
    
    html.Div(
        dcc.Dropdown(id='dropdown_linguagens',
        options=[{'label': 'Java', 'value': 'Java'},
                 {'label': 'Python', 'value': 'Python'},
                 {'label': 'SQL', 'value': 'SQL'},
                 {'label': 'GoLand', 'value': 'GoLand'},
                 {'label': 'JavaScript', 'value': 'JavaScript'},
                 {'label': 'ShellScript', 'value': 'ShellScript'},
                 {'label': 'PLSQL', 'value': 'PLSQL'},
                 {'label': 'Cobol', 'value': 'Cobol'},
                 {'label': 'PHP', 'value': 'PHP'},
                ], 
            value=['Java'],
            multi=True,
            style={'width': '50%', 'margin': '0 auto'}             
            )
        ), 
    dcc.Graph(
        id='scatter_plot'
    )
])

#_______________________________Callbacks____________________________________

@app.callback(
    Output('scatter_plot','figure'),
    [Input('dropdown_linguagens', 'value')]   
    
)

def atualizar_scatter(linguagens_selecionadas):
    
    scatter_trace = []
    
    for linguagem in linguagens_selecionadas:
        dados_linguagem = dados_conceitos[linguagem]
        for conceito, conhecimento in dados_linguagem.items():
            scatter_trace.append(
                go.Scatter(
                    x=[conceito],
                    y=[conhecimento],
                    mode='markers',
                    name=linguagem.title(),
                    marker=dict(size=30, color=color_map[linguagem]),
                    showlegend=False
                )
            )
            
    scatter_layout = go.Layout(
        title='Minhas Linguagens',
        xaxis=dict(title='Conceitos', showgrid=False),
        yaxis=dict(title='Nível de conhecimento', showgrid=False)
    )

    return {'data': scatter_trace, 'layout': scatter_layout}
if __name__ == '__main__':
    app.run_server(debug=True)

    
    

