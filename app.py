import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Datos
año = [2005 + i for i in range(19)]
e_petroleo = [
    15416919, 14881796, 15027399, 14233450, 12328866, 12607468, 12957860,
    15085772, 17334291, 18639623, 17907265, 16572386, 15722295, 14656979,
    12973942, 11770554, 11438199, 10189299, 8599810
]
e_gas = [
    12535.69, 13433.54, 14301.38, 14895.13, 12786.80, 14922.73, 16185.96,
    18475.14, 21021.44, 22187.95, 21998.81, 21144.53, 20531.91, 19178.87,
    16893.15, 16254.38, 16968.82, 15400.89, 13390.41
]
exportaciones_brasil_gn = [
    1400.9, 1619.4, 1453.9, 1020.5, 1285.6, 1643.3, 1363.3
]
e_gdolares = [
    1086.5, 1667.8, 1971.2, 3159.1, 1967.6, 2797.8, 3884.9, 5478.5, 6113.4,
    6011.1, 3770.4, 2049.1, 2581.3, 2970.4, 2719.9, 1989.3, 2249.1, 2973.4,
    2049.7
]
p_gas = [
    8.92, 6.72, 6.98, 8.86, 3.95, 4.39, 4.00, 2.75, 3.72, 4.37, 2.61, 2.49,
    2.96, 3.16, 2.57, 2.01, 3.85, 6.37, 2.54
]

# Crear DataFrame
df = pd.DataFrame({
    'Año': año,
    'Exportacion de petroleo (bariles)': e_petroleo,
    'Exportacion de gas (millones metros cubicos)': e_gas,
    'exp gn brasil (millones de dolares)': [None] * len(año),
    'exportaciones gas (millones de dolares)': e_gdolares
})
df.set_index('Año', inplace=True)
df.loc[2017:2024, 'exp gn brasil (millones de dolares)'] = exportaciones_brasil_gn

# Crear gráficos
fig1 = px.line(df, y='Exportacion de petroleo (bariles)', title='Exportaciones Petróleo (bariles)')
fig2 = px.line(df, y='Exportacion de gas (millones metros cubicos)', title='Exportaciones de Gas Natural (millones m³)')
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=df.index, y=df['exportaciones gas (millones de dolares)'], mode='lines', name='Exportación de Gas'))
fig3.add_trace(go.Scatter(x=df.index, y=df['exp gn brasil (millones de dolares)'], mode='lines', name='Exportación de Gas a Brasil'))
fig3.update_layout(title='Exportaciones de Gas Natural en Millones de Dólares (USD)')

fig4 = px.line(x=año, y=p_gas, title='Precio de Mercado del Gas en Dólares ($/mmbtu)',
    labels={
        'x': 'Año',         # Etiqueta del eje x
        'y': 'Precio ($/mmbtu)'  # Etiqueta del eje y
    })

# Aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([dbc.Col(html.H1("Dashboard de Exportaciones"), className="mb-3")]),
    dbc.Row([dbc.Col(dcc.Graph(figure=fig1), className="mb-3")]),
    dbc.Row([dbc.Col(dcc.Graph(figure=fig2), className="mb-3")]),
    dbc.Row([dbc.Col(dcc.Graph(figure=fig3), className="mb-3")]),
    dbc.Row([dbc.Col(dcc.Graph(figure=fig4), className="mb-3")]),
], fluid=True)

if __name__ == '__main__':
    app.run_server(port=4050,debug=True)