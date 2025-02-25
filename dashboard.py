import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

import os
import pandas as pd

tipos_colunas = {
    "ID": "int64",
    "Nome": "string",
    "Data": "datetime64[ns]",
    "Valor": "float64",
    "Ativo": "bool"
}


# Defina o caminho da pasta com os arquivos
pasta = "dados/atendimentos"

# Lista para armazenar os DataFrames
dataframes = []

# Percorre todos os arquivos da pasta
for arquivo in os.listdir(pasta):
    if arquivo.endswith(".xlsx"):  # Filtra apenas arquivos Excel
        caminho_completo = os.path.join(pasta, arquivo)
        df = pd.read_excel(caminho_completo, engine="openpyxl")  # Garante compatibilidade com arquivos modernos
        df["Arquivo"] = arquivo  # Adiciona nome do arquivo (opcional)
        dataframes.append(df)

df = pd.read_excel(caminho_completo, dtype=tipos_colunas, parse_dates=["Data"], engine="openpyxl")

# Inicializa o app com Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout com 3 colunas e componentes do Dash
app.layout = dbc.Container([
    dbc.Row([
        # Coluna 1: Entrada de Texto
        dbc.Col(html.Div([
            html.H4("Digite algo:"),
            dcc.Input(id="input-text", type="text", placeholder="Digite aqui...", className="form-control"),
            html.Br(), html.Br(),
            html.P("Texto digitado aparecerá aqui:", className="text-muted"),
            html.Div(id="output-text", className="border p-3")
        ], className="p-4 bg-light"), width=4),

        # Coluna 2: Slider + Gráfico
        dbc.Col(html.Div([
            html.H4("Ajuste o valor:"),
            dcc.Slider(id="slider", min=0, max=100, step=1, value=50,
                       marks={i: str(i) for i in range(0, 101, 20)}),
            html.Br(),
            dcc.Graph(id="graph")
        ], className="p-4 bg-white shadow"), width=4),

        # Coluna 3: Botão Interativo
        dbc.Col(html.Div([
            html.H4("Clique no botão:"),
            dbc.Button("Clique Aqui", id="btn-click", color="primary", className="mt-2"),
            html.Br(), html.Br(),
            html.Div(id="click-output", className="alert alert-info")
        ], className="p-4 bg-light"), width=4),
    ]),

    # Linha com gráfico de barras
    dbc.Row([
        dbc.Col(html.Div([
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
                    ],
                    'layout': {'title': 'Dash Data Visualization'}
                }
            )
        ], className="p-4 bg-light"), width=12),
    ])

], fluid=True)

# Rodando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
