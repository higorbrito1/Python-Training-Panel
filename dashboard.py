from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import glob

app = Dash()

arquivos = glob.glob('Dados/Extratos/*.xlsx')

dfs = [pd.read_excel(arquivo) for arquivo in arquivos]
df_final = pd.concat(dfs, ignore_index=True)

fig = px.bar(df_final, x="Data", y="Valor", color="Tipo Movimentação", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Brincando com Python'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
