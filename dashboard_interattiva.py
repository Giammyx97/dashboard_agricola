import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Carica i dati dal file CSV
df = pd.read_csv('dati_simulati.csv')

# Creazione dell'app Dash
app = dash.Dash(__name__)

# Layout della dashboard
app.layout = html.Div([
    html.H1("Dashboard di Monitoraggio Agricolo", style={'textAlign': 'center'}),

    html.Label("Seleziona una variabile da visualizzare:"),
    dcc.Dropdown(
        id='metric-selector',
        options=[
            {'label': 'Temperatura (°C)', 'value': 'Temperatura (°C)'},
            {'label': 'Umidità (%)', 'value': 'Umidità (%)'},
            {'label': 'Precipitazioni (mm)', 'value': 'Precipitazioni (mm)'},
            {'label': 'Raccolto (kg)', 'value': 'Raccolto (kg)'},
            {'label': 'Tempo di crescita (giorni)', 'value': 'Tempo di crescita (giorni)'},
            {'label': 'Efficienza (%)', 'value': 'Efficienza (%)'},
            {'label': 'Valore produzione (€)', 'value': 'Valore produzione (€)'},
            {'label': 'Costi totali (€)', 'value': 'Costi totali (€)'},
            {'label': 'Profitto (€)', 'value': 'Profitto (€)'}
        ],
        value='Raccolto (kg)',
        clearable=False
    ),

    dcc.Graph(id='data-graph')
])

# Callback per aggiornare il grafico
@app.callback(
    Output('data-graph', 'figure'),
    Input('metric-selector', 'value')
)
def update_graph(selected_metric):
    fig = px.line(df, x='Giorno', y=selected_metric, title=f"Andamento di {selected_metric}")
    return fig

# Avvio dell'app
if __name__ == '__main__':
    app.run(debug=True)
